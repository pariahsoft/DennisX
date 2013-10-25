DennisX
=======

DennisX (eXtensible) User-Managed MUD Server Kit

Copyright (c) 2013 PariahSoft LLC

Released under the MIT/Expat License.


Description
-----------

DennisX (Dennis eXtensible) is the third full overhaul (and second released version) of our Dennis project, which introduces an object oriented design and a plugin architecture for extending functionality. Like Dennis, DennisX is a user-managed MUD (multi-user dungeon) text adventure server. Users have complete control to modify any (unlocked) part of the game world.

The default server and plugin set include multiplayer facilities for world-building, exploration, and player interaction. Combat, monsters, NPCs, a player inventory, scripted events, and other features can be added to the API engine through the inclusion or development of additional plugins.

In Depth
--------

At its base, DennisX is an API engine with a mainloop and plugin manager. It provides a data management interface to the underlying game world structure, and is able to host plugins which can extend functionality, such as listener drivers, database drivers, and new user commands. User commands provide interfaces to the player for modifying and interacting with the game world and the data management interface. In addition, plugins can be written to add completely new features to the engine.

The default plugin set includes listener drivers for hosting as an IRC bot or a Telnet service, a JSON database driver for saving and restoring game data, and a basic collection of user commands for world exploration, interaction, and modification.
