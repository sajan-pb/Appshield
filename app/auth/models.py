from datetime import datetime
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    scans = db.relationship(
        "Scan",
        backref="user",
        lazy=True
    )


class Scan(db.Model):

    __tablename__ = "scans"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    scan_type = db.Column(
        db.String(20),
        nullable=False
    )

    target = db.Column(
        db.String(500),
        nullable=False
    )

    risk_score = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    findings = db.relationship(
        "Finding",
        backref="scan",
        lazy=True
    )


class Finding(db.Model):

    __tablename__ = "findings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    scan_id = db.Column(
        db.Integer,
        db.ForeignKey("scans.id"),
        nullable=False
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    severity = db.Column(
        db.String(20)
    )

    owasp_id = db.Column(
        db.String(20)
    )

    ai_explanation = db.Column(
        db.Text
    )