"""
Room user
Author: Alex (TheAmazingAussie)
"""

class RoomUser:
    def __init__(self, session):
        self.entity = session
        self.virtual_id = 0
        self.last_chat_id = 0
        self.dance_id = 0
        self.position = None
        self.goal = None
        self.rotation = 0
        self.head_rotation = 0
        self.statuses = {}
        self.path = []
        self.room = None
        self.is_walking = False
        self.needs_update = False
        self.is_loading_room = False
        self.chat_flood_timer = 0
        self.chat_count = 0

    def in_room(self):
        """
        Returns whever or not a user is actually fully loaded into a room
        :return:
        """

        return (self.is_loading_room == False) and (self.room is not None)

    def stop_walking(self, needs_update):
        """
        Stop user from walking
        :param needs_update:
        :return:
        """
        return

    def reset(self):
        """
        Reset all room user variables
        :return:
        """
        self.__init__(self.entity)

        print (self.room)

    def dispose(self):
        """
        Clear all room user data by calling the constructor
        :return: None
        """
        del self.entity
        del self.virtual_id
        del self.dance_id
        del self.position
        del self.goal
        del self.rotation
        del self.head_rotation
        del self.statuses
        del self.path
        del self.room
        del self.is_walking
        del self.needs_update
        del self.is_loading_room
        del self.chat_flood_timer
        del self.chat_count
