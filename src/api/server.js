import path from 'path'
import hapi from '@hapi/hapi'

import { config } from '~/src/config/index.js'
import { router } from '~/src/api/router.js'
import { requestLogger } from '~/src/helpers/logging/request-logger.js'
import { mongoDb } from '~/src/helpers/mongodb.js'
import { failAction } from '~/src/helpers/fail-action.js'
import { secureContext } from '~/src/helpers/secure-context/index.js'
import { pulse } from '~/src/helpers/pulse.js'

async function createServer() {
  const server = hapi.server({
    port: config.get('port'),
    routes: {
      validate: {
        options: {
          abortEarly: false
        },
        failAction
      },
      files: {
        relativeTo: path.resolve(config.get('root'), '.public')
      },
      security: {
        hsts: {
          maxAge: 31536000,
          includeSubDomains: true,
          preload: false
        },
        xss: 'enabled',
        noSniff: true,
        xframe: true
      }
    },
    router: {
      stripTrailingSlash: true
    }
  })

  // Hapi Plugins:
  // requestLogger - automatically logs incoming requests
  // secureContext - loads CA certificates from environment config
  // pulse         - provides shutdown handlers
  // mongoDb       - sets up mongo connection pool and attaches to `server` and `request` objects
  // router        - routes used in the app
  await server.register([requestLogger, secureContext, pulse, mongoDb, router])

  return server
}

export { createServer }