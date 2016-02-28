class AmpMiddleware(object):
    def process_request(self, request):
        request.is_amp = False

        if '/amp/' in request.path:
            request.is_amp = True
        return None
