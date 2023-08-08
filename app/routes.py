from flask import Blueprint, request, make_response
import db.DAO.sounds_DAO as sounds_DAO
import db.DAO.times_DAO as times_DAO
from sound_model.run_model import run_model

routes = Blueprint("routes", __name__)

@routes.route('/video', methods=["POST"])
def processVideo():
    data = request.get_json()
    videoId = data.get("videoId", None)
    run_model(videoId)
    return make_response('', 204)

@routes.route('/sounds', methods=["GET"])
def getSupportedSounds():
    return sounds_DAO.getSupportedSounds()

@routes.route('/times', methods=["POST"])
def getMuteTimes():
    data = request.get_json()
    videoId = data.get("videoId", None)
    sounds = data.get("sounds", [])
    return times_DAO.getMuteTimes(videoId, sounds)