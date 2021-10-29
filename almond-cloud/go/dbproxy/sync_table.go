// Copyright 2021 The Board of Trustees of the Leland Stanford Junior University
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
package dbproxy

import (
	"almond-cloud/sql"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func syncTableGetAll(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	rows := m.NewRows()
	if err := syncTable.GetAll(rows, userID); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": rows})
}

func syncTableGetOne(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	row, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	key, err := parseKey(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	row.SetKey(*key)
	if err := syncTable.GetOne(row); err != nil {
		if err == gorm.ErrRecordNotFound {
			c.JSON(http.StatusNotFound, gin.H{"error": "row not found"})
		} else {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		}
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": row})
}

func syncTableGetRaw(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	rows, err := syncTable.GetRaw(m, userID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": rows})
}

func syncTableGetChangesAfter(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	lastModified, err := strconv.ParseInt(c.Param("millis"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	rows, err := syncTable.GetChangesAfter(m, lastModified, userID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": rows})
}

func syncTableHandleChanges(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	rows := m.NewSyncRecords()
	if err := c.ShouldBindJSON(rows); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	srows, err := sql.ToSyncRecordSlice(rows)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	results, err := syncTable.HandleChanges(srows, userID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": results})
}

func syncTableSyncAt(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	lastModified, err := strconv.ParseInt(c.Param("millis"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	rows := m.NewSyncRecords()
	if err := c.ShouldBindJSON(rows); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	srows, err := sql.ToSyncRecordSlice(rows)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	m.SetKey(sql.Key{UserID: userID})
	latest, ourChanges, done, err := syncTable.SyncAt(m.NewSyncRecord(lastModified), srows)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	ret := struct {
		LastModified int64            `json:"lastModified"`
		OurChanges   []sql.SyncRecord `json:"ourChanges"`
		Done         []bool           `json:"done"`
	}{latest, ourChanges, done}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": ret})
}

func syncTableReplaceAll(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	userID, err := parseUserID(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	rows := m.NewSyncRecords()
	if err := c.ShouldBindJSON(rows); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	srows, err := sql.ToSyncRecordSlice(rows)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if err := syncTable.ReplaceAll(srows, userID); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": true})
}

func syncTableInsertIfRecent(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	key, err := parseKey(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if err := c.ShouldBindJSON(m); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	m.SetKey(*key)

	lastModified, err := strconv.ParseInt(c.Param("millis"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	done, err := syncTable.InsertIfRecent(m, lastModified)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": done})
}

func syncTableInsertOne(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	key, err := parseKey(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	if err := c.ShouldBindJSON(m); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	m.SetKey(*key)
	lastModified, err := syncTable.InsertOne(m)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": lastModified})
}

func syncTableDeleteIfRecent(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	key, err := parseKey(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	if err := c.ShouldBindJSON(m); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	lastModified, err := strconv.ParseInt(c.Param("millis"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	m.SetKey(*key)
	done, err := syncTable.DeleteIfRecent(m, lastModified)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": done})
}

func syncTableDeleteOne(c *gin.Context) {
	syncTable := sql.GetSyncTable()
	m, ok := sql.NewSyncRow(c.Param("name"))
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "table name not found"})
		return
	}
	key, err := parseKey(c)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	m.SetKey(*key)
	lastModified, err := syncTable.DeleteOne(m)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": "ok", "data": lastModified})
}
