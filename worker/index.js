// Redirects www.romegolfcartguide.com to romegolfcartguide.com, then serves the static site.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "www.romegolfcartguide.com") {
      url.hostname = "romegolfcartguide.com";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
