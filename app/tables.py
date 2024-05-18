import datetime
import sys
import typing as t
import uuid
from decimal import Decimal
from enum import Enum

from piccolo.table import Table
from piccolo.columns import (JSON, Boolean, ForeignKey, Integer, Interval, 
                             Numeric, Timestamp, UUID, Varchar)
from piccolo.columns.readable import Readable


class Manager(Table):
    name = Varchar(length=100)
    email = Varchar(length=150)
    phonenum = Varchar(20)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s",
            columns=[cls.name],
        )

class Band(Table):
    name = Varchar(length=100)
    manager = ForeignKey(references=Manager)
    popularity = Integer()

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s",
            columns=[cls.name],
        )
    

class Venue(Table):
    name = Varchar(length=100)
    capacity = Integer(default=0)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s",
            columns=[cls.name],
        )
    

class Concert(Table):
    band_1 = ForeignKey(references=Band)
    band_2 = ForeignKey(references=Band)
    venue = ForeignKey(references=Venue)
    starts = Timestamp()
    duration = Interval()

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s and %s at %s",
            columns=[
                cls.band_1.name,
                cls.band_2.name,
                cls.venue.name,
            ],
        )

class Ticket(Table):
    class TicketType(Enum):
        sitting = "sitting"
        standing = "standing"
        premium = "premium"

    concert = ForeignKey(Concert)
    price = Numeric(digits=(5, 2))
    ticket_type = Varchar(choices=TicketType, default=TicketType.standing)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s - %s",
            columns=[
                t.cast(t.Type[Venue], cls.concert.venue).name,
                cls.ticket_type,
            ],
        )


class DiscountCode(Table):
    code = UUID()
    active = Boolean(default=True, null=True)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s - %s",
            columns=[cls.code, cls.active],
        )


class RecordingStudio(Table):
    name = Varchar()
    facilities = JSON(null=True)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s",
            columns=[cls.name],
        )
