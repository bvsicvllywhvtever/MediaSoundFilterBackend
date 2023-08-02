from flask import Blueprint

routes = Blueprint("routes", __name__)

@routes.route('/sounds')
def getSupportedSounds():
    return []

@routes.route('/times')
def getMuteTimes(videoId, sounds):
    return []