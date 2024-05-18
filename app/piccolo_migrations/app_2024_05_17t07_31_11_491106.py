from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from enum import Enum
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Boolean
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Interval
from piccolo.columns.column_types import JSON
from piccolo.columns.column_types import Numeric
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import UUID
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.interval import IntervalCustom
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table
import decimal


class Band(Table, tablename="band", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class Concert(Table, tablename="concert", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class Manager(Table, tablename="manager", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class Venue(Table, tablename="venue", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2024-05-17T07:31:11:491106"
VERSION = "1.5.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="app", description=DESCRIPTION
    )

    manager.add_table(
        class_name="Ticket", tablename="ticket", schema=None, columns=None
    )

    manager.add_table(
        class_name="Manager", tablename="manager", schema=None, columns=None
    )

    manager.add_table(
        class_name="Venue", tablename="venue", schema=None, columns=None
    )

    manager.add_table(
        class_name="Band", tablename="band", schema=None, columns=None
    )

    manager.add_table(
        class_name="RecordingStudio",
        tablename="recording_studio",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="DiscountCode",
        tablename="discount_code",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="Concert", tablename="concert", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="Ticket",
        tablename="ticket",
        column_name="concert",
        db_column_name="concert",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Concert,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Ticket",
        tablename="ticket",
        column_name="price",
        db_column_name="price",
        column_class_name="Numeric",
        column_class=Numeric,
        params={
            "default": decimal.Decimal("0"),
            "digits": (5, 2),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Ticket",
        tablename="ticket",
        column_name="ticket_type",
        db_column_name="ticket_type",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "standing",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": Enum(
                "TicketType",
                {
                    "sitting": "sitting",
                    "standing": "standing",
                    "premium": "premium",
                },
            ),
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Manager",
        tablename="manager",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Manager",
        tablename="manager",
        column_name="email",
        db_column_name="email",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 150,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Manager",
        tablename="manager",
        column_name="phonenum",
        db_column_name="phonenum",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Venue",
        tablename="venue",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Venue",
        tablename="venue",
        column_name="capacity",
        db_column_name="capacity",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Band",
        tablename="band",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Band",
        tablename="band",
        column_name="manager",
        db_column_name="manager",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Manager,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Band",
        tablename="band",
        column_name="popularity",
        db_column_name="popularity",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="RecordingStudio",
        tablename="recording_studio",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="RecordingStudio",
        tablename="recording_studio",
        column_name="facilities",
        db_column_name="facilities",
        column_class_name="JSON",
        column_class=JSON,
        params={
            "default": "{}",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="DiscountCode",
        tablename="discount_code",
        column_name="code",
        db_column_name="code",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="DiscountCode",
        tablename="discount_code",
        column_name="active",
        db_column_name="active",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": True,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Concert",
        tablename="concert",
        column_name="band_1",
        db_column_name="band_1",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Band,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Concert",
        tablename="concert",
        column_name="band_2",
        db_column_name="band_2",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Band,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Concert",
        tablename="concert",
        column_name="venue",
        db_column_name="venue",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Venue,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Concert",
        tablename="concert",
        column_name="starts",
        db_column_name="starts",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Concert",
        tablename="concert",
        column_name="duration",
        db_column_name="duration",
        column_class_name="Interval",
        column_class=Interval,
        params={
            "default": IntervalCustom(
                weeks=0,
                days=0,
                hours=0,
                minutes=0,
                seconds=0,
                milliseconds=0,
                microseconds=0,
            ),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
