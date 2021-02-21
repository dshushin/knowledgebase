FROM node:15.8.0-alpine

WORKDIR /app

COPY package.json package.json
COPY yarn.lock yarn.lock
RUN yarn install

COPY tsconfig.json tsconfig.json
COPY public public
COPY src src

CMD ["yarn", "start"]