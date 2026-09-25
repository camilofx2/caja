-- Registro automático por SMS (Bancolombia). Pegar en Supabase → SQL Editor → Run.

-- Clave personal de cada usuario (la usa el Atajo del iPhone para enviar SMS a tu bandeja)
create table if not exists public.caja_keys (
  user_id    uuid primary key default auth.uid() references auth.users on delete cascade,
  key        text unique not null,
  created_at timestamptz not null default now()
);
alter table public.caja_keys enable row level security;
drop policy if exists "mi clave" on public.caja_keys;
create policy "mi clave" on public.caja_keys for all to authenticated
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
grant select, insert, update, delete on public.caja_keys to authenticated;

-- Bandeja "Por confirmar": SMS del banco que llegan y esperan tu confirmación
create table if not exists public.caja_inbox (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null default auth.uid() references auth.users on delete cascade,
  raw        text not null check (length(raw) between 5 and 1000),
  source     text not null default 'sms',
  created_at timestamptz not null default now(),
  unique (user_id, raw)
);
alter table public.caja_inbox enable row level security;
drop policy if exists "mi bandeja" on public.caja_inbox;
create policy "mi bandeja" on public.caja_inbox for all to authenticated
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
grant select, insert, delete on public.caja_inbox to authenticated;
alter publication supabase_realtime add table public.caja_inbox;

-- Receptor: el Atajo envía el SMS con tu clave en el encabezado "x-clave".
-- Solo puede AGREGAR mensajes a tu bandeja; no puede leer nada.
create or replace function public.caja_capture(msg text) returns text
language plpgsql security definer set search_path = public as $$
declare k text; u uuid;
begin
  k := coalesce(current_setting('request.headers', true)::json->>'x-clave', '');
  if length(k) < 20 then raise exception 'clave inválida' using errcode = '28000'; end if;
  select user_id into u from caja_keys where key = k;
  if u is null then raise exception 'clave inválida' using errcode = '28000'; end if;
  if msg is null or length(msg) < 5 or length(msg) > 1000 then raise exception 'mensaje inválido'; end if;
  insert into caja_inbox(user_id, raw, source) values (u, msg, 'sms') on conflict (user_id, raw) do nothing;
  return 'ok';
end $$;
revoke all on function public.caja_capture(text) from public;
grant execute on function public.caja_capture(text) to anon, authenticated;
