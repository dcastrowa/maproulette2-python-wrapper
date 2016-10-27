#!/usr/bin/env python

import os
import json
import requests

class MapRouletteObject(object):
    """Abstract MapRoulette base class"""

    # TODO use ABC?

    @property
    def path(self):
        raise NotImplementedError()

    def get(self, server, use_api_key=False):
        return server.get(self.path, use_api_key)

    def post(self, server):
        return server.post(self.path, self.__str__())

    def put(self, server):
        return server.put(self.path, self.__str__())

    def delete(self, server):
        return server.delete()


class Project(MapRouletteObject):
    """A MapRoulette Project."""

    READONLY = ["id"]

    @property
    def path(self):
        return os.path.join("project", str(self._id))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def __init__(self, id=None):
        self._id = id
        self._name = None
        self._description = None
        self._enabled = None

    def __str__(self):
        return json.dumps({
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "enabled": self._enabled
        })



    #TODO support groups


class Challenge(MapRouletteObject):

    READONLY = ["id", "featured"]

    @property
    def path(self):
        return os.path.join("challenge", self._id)

    @property
    def id(self):
        """The identifier that MapRoulette assigns to the Challenge."""
        return self._id

    @property
    def name(self):
        """The name for the Challenge."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        """The description for the Challenge."""
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def instruction(self):
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def difficulty(self):
        """The challenge's difficulty"""
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def blurb(self):
        """The challenge Blurb (short description)"""
        return self._blurb

    @blurb.setter
    def blurb(self, value):
        self._blurb = value

    @property
    def enabled(self):
        """Whether the Challenge is Enabled or not"""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def challenge_type(self):
        """The type of Challenge"""
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self._challenge_type = value

    @property
    def featured(self):
        """Whether the Challenge is Featured in MapRoulette. Only a superuser can set this."""
        return self._featured

    @featured.setter
    def featured(self, value):
        self._featured = value

    @property
    def default_priority(self):
        return self._default_priority

    @default_priority.setter
    def default_priority(self, value):
        self._default_priority = value

    @property
    def default_zoom(self):
        return self._default_zoom

    @default_zoom.setter
    def default_zoom(self, value):
        self._default_zoom = value

    @property
    def min_zoom(self):
        return self._min_zoom

    @min_zoom.setter
    def min_zoom(self, value):
        self._min_zoom = value

    @property
    def max_zoom(self):
        return self._max_zoom

    @max_zoom.setter
    def max_zoom(self, value):
        self._max_zoom = value

    def __init__(self, id=None):
        super(Challenge, self).__init__()
        self._id = id
        self._name = None
        self._description = None
        self._parent = None
        self._instruction = None
        self._difficulty = None
        self._blurb = None
        self._enabled = False
        self._challenge_type = None
        self._featured = None
        self._default_priority = None
        self._default_zoom = None
        self._min_zoom = None
        self._max_zoom = None

    def __str__(self):
        return json.dumps([{
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "parent": self._parent,
            "instruction": self._instruction,
            "difficulty": self._difficulty,
            "blurb": self._blurb,
            "enabled": self._enabled,
            "challengeType": self._challenge_type,
            "featured": self._featured,
            "defaultPriority": self._default_priority,
            "defaultZoom": self._default_zoom,
            "minZoom": self._min_zoom,
            "maxZoom": self._max_zoom
        }])


class ChallengeCollection(object):
    """A collection of Challenges"""

    @property
    def challenges(self):
        return self._challenges

    @challenges.setter
    def challenges(self, value):
        self._challenges = value

    def add_challenge(self, challenge):
        self._challenges.append(challenge)

    def __init__(self):
        super(ChallengeCollection, self).__init__()
        self._challenges = []

    def __str__(self):
        return json.dumps(challenges)

    # TODO init with challenges JSON

class Task(MapRouletteObject):

    READONLY = ["id"]

    @property
    def paths(self):
        return os.path.join("task", str(self._id))

    @property
    def id(self):
        """The task identifier, as assigned by MapRoulette"""
        return self._id

    @property
    def name(self):
        """The name of the task that you want to assign"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def parent(self):
        """The id of the parent Challenge"""
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def instruction(self):
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def __init__(self, id=None):
        super(Task, self).__init__()
        self._id = id
        self._name = None
        self._parent = None
        self._instruction = None
        self._location = None

    def __str__(self):
        return json.dumps([{
            "id": self._id,
            "name": self._name,
            "parent": self._parent,
            "instruction": self._instruction,
            "location": self._location
        }])


class TaskCollection(object):
    """A collection of Tasks"""

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

    def add_task(self, task):
        self._tasks.append(task)

    def __init__(self):
        super(TaskCollection, self).__init__()
        self._tasks = []

    def __str__(self):
        return json.dumps(tasks)


class Server(object):
    """MapRoulette server instance"""

    def __init__(self, api_key, project_id, base_url="http://maproulette.org/api/v2"):
        super(Server, self).__init__()
        self.base_url = base_url
        self.project_id = project_id
        self.headers = {"apiKey": api_key}

    def get(self, path, use_api_key):
        if use_api_key:
            response = requests.get(
                os.path.join(self.base_url, path),
                headers=self.headers)
        else:
            response = requests.get(os.path.join(self.base_url, path))
        if response.status_code == 200:
            return response.json()
        raise MaprouletteException()

    def post(self, path, payload):
        response = requests.post(
            os.path.join(self.base_url, path),
            data=payload,
            headers=self.headers)
        return response.json()

    def put(self, path, payload):
        response = requests.put(
            os.path.join(self.base_url, path),
            data=payload,
            headers=self.headers)
        return response.json()

    def delete(self, path):
        response = requests.delete(
            os.path.join(self.base_url, path),
            headers=self.headers)
        return response.json()

    def my_challenges(self):
        response = requests.get(
            os.path.join(
                self.base_url,
                "project",
                self.project_id,
                "challenges"),
            headers=self.headers
        )
        return response.json()


class MaprouletteException(Exception):
    """MapRoulette API Exception"""
    pass
