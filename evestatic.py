# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""evestatic.py: """

import sqlite3


class StaticDB(object):
    def __init__(self):
        self._connection = sqlite3.connect('evestatic.db')
        self._cursor = self._connection.cursor()

    def __del__(self):
        self._connection.close()

    def skill_id(self, skill_name):
        self._cursor.execute("SELECT typeID FROM invtypes"
                             " WHERE typeName = :name",
                             {'name': skill_name})
        result = self._cursor.fetchone()
        self._cursor.fetchall()
        return result[0]

    def skill_name(self, skillID):
        self._cursor.execute("SELECT typeName"
                             " FROM invtypes WHERE typeID = :id",
                             {'id': skillID})
        result = self._cursor.fetchone()
        self._cursor.fetchall()
        return result[0]

    def skill_group(self, skillID):
        self._cursor.execute("SELECT g.marketGroupName"
                             " FROM invtypes t"
                             " JOIN invmarketgroups g"
                             " ON t.marketGroupID = g.marketGroupID"
                             " WHERE t.typeID = :id",
                             {'id': skillID})
        result = self._cursor.fetchone()
        self._cursor.fetchall()
        return result[0]