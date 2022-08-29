from flask import Blueprint, request, jsonify

from core.auth import token_required
from core.database import db
from core.models import Event, User, UserEvent
from event.serializer import EventSerializer, EventInvitationSerializer, ResponseInvitationSerializer

event_router = Blueprint("event", __name__, url_prefix="/event")


@event_router.route("")
@token_required
def get(user):
    schema = EventSerializer(many=True)
    events = Event.query.filter(Event.users.any(User.id == user.id))
    # db.session.query(Event).join(UserEvent).filter(UserEvent.user_id == user.id)
    # SELECT * FROM event JOIN user_event ON event.id = user_event.event_id WHERE user_event.user_id = 1
    profile_json = schema.dump(events)
    return jsonify(profile_json)


@event_router.route("/<int:event_id>", methods=["GET"],)
@token_required
def retrieve(user, event_id):
    schema = EventSerializer()
    events = Event.query.filter(Event.users.any(User.id == user.id)).filter(Event.id == event_id).first()
    profile_json = schema.dump(events)
    return jsonify(profile_json)


@event_router.route("", methods=["POST"],)
@token_required
def create(user):
    data = request.get_json()
    schema = EventSerializer()
    event_data = schema.load(data)
    user_chek = User.query.filter(User.id == user.id).first()
    if not user_chek:
        return "User not found"
    else:
        event_obj = Event(
            name=event_data["name"],
            description=event_data["description"],
            starts_at=event_data["starts_at"],
            ends_at=event_data["ends_at"],
            creator_id=event_data["creator_id"]
        )
        event_obj.users.append(user)
        db.session.add(event_obj)
        db.session.commit()
        event_json = schema.dump(event_obj)
        return event_json


@event_router.route("/<int:event_id>", methods=["PUT"],)
@token_required
def edit(user, event_id):
    user_chek = User.query.filter(User.id == user.id).first()
    if not user_chek:
        return "User not found"
    else:
        data = request.get_json()
        schema = EventSerializer()
        event_data = schema.load(data)
        event_for_edit = Event.query.filter(Event.users.any(User.id == user.id)).filter(Event.id == event_id).\
            filter(Event.creator_id == user.id).first()
        if not event_for_edit:
            return "Event not found"
        else:
            event_for_edit.name = event_data["name"]
            event_for_edit.description = event_data["description"]
            event_for_edit.starts_at = event_data["starts_at"]
            event_for_edit.ends_at = event_data["ends_at"]
            db.session.commit()
            event_json = schema.dump(event_for_edit)
            return event_json


@event_router.route("/<int:event_id>", methods=["DELETE"],)
@token_required
def delete(user, event_id):
    user_chek = User.query.filter(User.id == user.id).first()
    if not user_chek:
        return "User not found"
    else:
        event_for_del = Event.query.filter(Event.users.any(User.id == user.id)).filter(Event.id == event_id).\
            filter(Event.creator_id == user.id).first()
        if not event_for_del:
            return "Event not found"
        else:
            db.session.delete(event_for_del)
            db.session.commit()
            return "Event deleted"


@event_router.route("/<int:event_id>/invite", methods=["POST"])
@token_required
def invite(user, event_id):
    data = request.get_json()
    event_schema = EventSerializer()
    invitation_schema = EventInvitationSerializer()
    invitation_data = invitation_schema.load(data)
    event = Event.query.filter(
        Event.users.any(
            User.id == user.id
        )
    ).filter(Event.id == event_id).filter(Event.creator_id == user.id).first()
    if not event:
        return "Event not found"

    for user_id in invitation_data["users_id"]:
        invited_user = User.query.get(user_id)
        if invited_user:
            event.users.append(invited_user)

    db.session.add(event)
    db.session.commit()
    event_json = event_schema.dump(event)
    return event_json


@event_router.route("/<int:event_id>/invite", methods=["PUT"])
@token_required
def response_to_invitation(user, event_id):
    user_chek = User.query.filter(User.id == user.id).first()
    if not user_chek:
        return "User not found"
    else:
        event = Event.query.filter(Event.users.any(User.id == user.id)).\
            filter(Event.id == event_id).first()
        if not event:
            return "Event not found"
        else:
            data = request.get_json()
            response_schema = ResponseInvitationSerializer()
            response_data = response_schema.load(data)
            response_user_event = UserEvent.query.filter(UserEvent.user_id == user.id).\
                filter(UserEvent.event_id == event_id).first()
            response_user_event.invitation_status = response_data["invitation_status"]
            db.session.commit()
            response_json = response_schema.dump(response_user_event)
            return response_json
