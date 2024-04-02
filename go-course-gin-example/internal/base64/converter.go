package base64

import (
	_base64 "encoding/base64"
	"errors"
	"net/http"

	"github.com/gin-gonic/gin"
)

var errBadRequest = errors.New("bad request")

type handler struct{}

func (h handler) decode(c *gin.Context) {
	base64, ok := c.GetQuery("base64")
	if !ok {
		c.AbortWithError(http.StatusBadRequest, errBadRequest)
		return
	}
	decoded, err := _base64.StdEncoding.DecodeString(base64)
	if err != nil {
		c.AbortWithError(http.StatusBadRequest, err)
		return
	}
	c.String(http.StatusOK, string(decoded))
}

func (h handler) encode(c *gin.Context) {
	text, ok := c.GetQuery("text")
	if !ok {
		c.AbortWithError(http.StatusBadRequest, errBadRequest)
		return
	}
	encoded := _base64.StdEncoding.EncodeToString([]byte(text))
	c.String(http.StatusOK, encoded)
}
