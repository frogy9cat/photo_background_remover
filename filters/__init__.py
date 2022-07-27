from aiogram import Dispatcher

from loader import dp
from . import PrivateFilter


if __name__ == "filters":
    dp.filters_factory.bind(PrivateFilter.IsPrivate)
