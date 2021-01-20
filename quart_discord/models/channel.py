from .base import DiscordModelsBase
from quart import current_app

import discord
from .. import configs


class Channel(DiscordModelsBase):
    """Represents a Discord Guild Channel.
    Operations
    ----------
    x == y
        Checks if two channels are equal.
    x != y
        Checks if two channels are not equal.
    str(x)
        Returns the channel's name.
    Attributes
    ----------
    id `int`
        The id of this channel
    
    name `str`
        The name of the channel (2-100 characters)
    
    type `int`
        The type of channel
    
    guild_id `int`
        The id of the guild
    
    position `int`
        Sorting position of the channel
    
    topic `str`
        The channel topic (0-1024 characters)
    
    nsfw `bool`
        Whether the channel is nsfw
    
    permissions_overwrites `list`
        Explicit permission overwrites for members and roles
    
    rate_limit `int`
        Amount of seconds a user has to wait before sending another 
        message (0-21600); bots, as well as users with the permission 
        manage_messages or manage_channel, are unaffected
    """
    def __init__(self, data):
        self.id = int(data['id'])
        self.name = data['name']
        self.type = data['type']
        self.guild_id = data['guild_id']
        self.position = data['position']
        self.topic = data['topic']
        self.nsfw = data['nsfw']
        self.permission_overwrites = data['permission_overwrites']
        self.rate_limit = data['rate_limit_per_user']

    def __eq__(self, other_channel):
            return isinstance(other_channel, Channel) and other_channel.id == self.id

    def __ne__(self, other_channel):
        return not self.__eq__(other_channel)

    def __str__(self):
        return self.name
