from abc import ABCMeta, abstractmethod

class BaseModel:
	
	__metaclass__ = ABCMeta
	
	_id = None	# UUID class needed for id...
	_isNew = None
	_isDirty = None
	_toUpdateFiledNames = []
	
	__INSERT_PREAMBLE = "INSERT INTO "
	__INSERT_VALUES_PREAMBLE = " VALUES "
	__UPDATE_PREAMBLE = "UPDATE %s SET"
	__DELETE_COMMAND_FORMAT = "DELETE FROM %s WHERE %s = ?"

	# Need to create 'BaseRepositoryInterface' class in order to implement 'repository' attribute

	# use getattr() to get class atributes
	# use setattr() to set class attributes

	def propertyChanged (fieldName):
		if not _isDirty:
			_isDirty = True
		
		if _toUpdateFiledNames.index(fieldName) < 0:
			_toUpdateFiledNames.append(fieldName)

	def hasChanged ():
		return _isNew or (_isDirty and (len(_toUpdateFiledNames) > 0))

	def stringHasChanged (string1, string2):
		return string1 != string2

	def stringHasChangedIgnoreCase (string1, string2):
		return string1.lower() != string2.lower() 

	def uuidHasChanged (uuid1, uuid2):
		return uuid1 != uuid2

	def uuidHasChangedIgnoreCase (uuid1, uuid2):
		return uuid1.lower() != uuid2.lower() 

	def localDateTimeHasChanged (localDateTime1, localDateTime2):
		return localDateTime1 != localDateTime2

	def byteArrayHasChanged (byteArray1, byteArray2):
		changed = len(byteArray1) != len(byteArray2)

		if not changed:
			for i in range (0, len(byteArray1)):
				if byteArray1[i] != byteArray2[i]:
					changed = true
					break

		return changed

	def hashCode ():
		result = 1
		prime = 31

		# UUID class needed for id...
		return (prime * result) + (0 if id == None else id.hashCode())

	# Do we need to implement the 'equals()' method for the Python implementation?

	# Prof has constructors for his abstract class. Wut.

	# Don't know how to implement:
	# protected abstract void fillFromRecord(ResultSet rs) throws SQLException;
	# protected abstract Map<String, Object> fillRecord(Map<String, Object> record);
	# public void load(ResultSet rs) throws SQLException
	# load(ResultSet rs)
	# onIdSe()t ?
	# onLoadComplete(String connectionString) ?
	# save() methods
	# insertNewRecord(Connection connection)
	# PreparedStatement buildInsertStatement(Map<String, Object> record, Connection connection)
	# updateRecord(Connection connection)
	# PreparedStatement buildUpdateStatement(Map<String, Object> record, Connection connection)
	# delete() methods
	# ConnectAndRun(Consumer<Connection> action)
	# Constructors (why)
	# literally everything pertaining to sql
	# literally everything




