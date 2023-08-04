from flask import Blueprint, request
import db.DAO.sounds_DAO as sounds_DAO
import db.DAO.times_DAO as times_DAO

routes = Blueprint("routes", __name__)

@routes.route('/sounds', methods=["GET"])
def getSupportedSounds():
    return sounds_DAO.getSupportedSounds()

@routes.route('/times', methods=["POST"])
def getMuteTimes():
    data = request.get_json()
    videoId = data.get("videoId", None)
    sounds = data.get("sounds", [])
    return times_DAO.getMuteTimes(videoId, sounds)