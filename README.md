# AirBnB_Clone


This is a project to clone an AirBnB.

## About
The first step undertaken is to write a command interpreter to manage all the AirBnB objects.

All the tasks are linked and are set out to achieve the following:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
    
The command interpreter referred to as the console helps to manage the objects of the project in the following ways:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
    
## Contributors
Contributors to the project are Warren Mulubi and Tom Alata also stated in the AUTHORS file.
