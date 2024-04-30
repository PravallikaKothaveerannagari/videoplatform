import createClient from 'openapi-fetch'
import type { paths } from './v1'

const BASE_URL = import.meta.env.DEV ? 'http://127.0.0.1:8000' : 'https://plvids.azurewebsites.net'

export function client() {
  const token = localStorage.getItem('token_video_platform_7348734')
  return token
    ? createClient<paths>({
        baseUrl: BASE_URL,
        headers: { Authorization: `Token ${token}` }
      })
    : createClient<paths>({ baseUrl: BASE_URL })
}
