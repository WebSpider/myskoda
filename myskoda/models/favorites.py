"""MySkoda Favorite place models."""

from dataclasses import dataclass, field
from enum import StrEnum

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from .common import BaseResponse, Coordinates


class FavoriteType(StrEnum):
    LOCATION = "LOCATION"


@dataclass
class PlaceDetail(DataClassORJSONMixin):
    place_id: str = field(metadata=field_options(alias="placeId"))
    gps_coordinates: Coordinates = field(metadata=field_options(alias="gpsCoordinates"))
    formatted_address: str | None = field(
        default=None, metadata=field_options(alias="formattedAddress")
    )
    name: str | None = field(default=None)


@dataclass
class FavoritePlace(DataClassORJSONMixin):
    place_type: FavoriteType = field(metadata=field_options(alias="type"))
    id: str
    place_detail: PlaceDetail = field(metadata=field_options(alias="placeDetail"))


@dataclass
class FavoritePlaces(BaseResponse):
    places: list[FavoritePlace]
    errors: list
