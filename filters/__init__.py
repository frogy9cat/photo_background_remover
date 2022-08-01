from aiogram import Dispatcher

from loader import dp
from . import AdminFilter
from . import PrivateFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter.IsAdmin)
    dp.filters_factory.bind(PrivateFilter.IsPrivate)
    
