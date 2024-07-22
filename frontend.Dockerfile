FROM node:20-slim AS base
ENV PATH="$PNPM_HOME:$PATH"

FROM base AS build
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN --mount=type=cache,id=npm,target=/npm/store npm i
RUN npm run build

FROM base AS app
COPY --from=build /usr/src/app /prod/app
WORKDIR /prod/app
EXPOSE 3000
CMD [ "node", "build" ]
