import enum

from core.database import db

class EventStatus(enum.Enum):
    pending = 'pending'
    accepted = 'accepted'
    declined = 'declined'


class UserEvent(db.Model):
    __tablename__ = "user_event"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    invitation_status = db.Column(db.Enum(EventStatus), default=EventStatus.pending.value,
                                  server_default=EventStatus.pending.value, nullable=False)
