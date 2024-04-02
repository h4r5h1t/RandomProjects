package unixtime

import (
	"net/http"
	"strconv"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

type handler struct{}

func (h handler) toHuman(c *gin.Context) {
	timestamp := c.Param("timestamp")
	parsedTimeStamp, err := strconv.ParseInt(timestamp, 10, 64)
	if err != nil {
		c.AbortWithError(http.StatusBadRequest, err)
		return
	}
	tm := time.Unix(parsedTimeStamp, 0)

	response := strings.TrimSpace(tm.String()) // Trim trailing whitespace from the response
	c.String(http.StatusOK, response)

	// c.String(http.StatusOK, tm.String())
}
