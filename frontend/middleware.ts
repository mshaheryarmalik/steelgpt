// export { auth as middleware } from './auth'

export default function middleware(req: any, res: any, next: any) {
  // next()
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
}
