-- Pega todo esto en Supabase → SQL Editor → New query → Run.
-- Crea la tabla donde viven tus datos y la protege para que solo tu usuario pueda leerlos o cambiarlos.

create table if not exists public.caja_docs (
  user_id    uuid        not null default auth.uid() references auth.users on delete cascade,
  id         text        not null,
  body       jsonb       not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, id)
);

alter table public.caja_docs enable row level security;

drop policy if exists "solo mis datos" on public.caja_docs;
create policy "solo mis datos" on public.caja_docs
  for all to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);

grant select, insert, update, delete on public.caja_docs to authenticated;

-- Cambios en vivo entre iPhone y Mac
alter publication supabase_realtime add table public.caja_docs;
