#!/usr/bin/python3
"""__init__ for reload the storge"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
