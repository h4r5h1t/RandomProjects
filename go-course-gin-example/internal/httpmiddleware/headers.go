package httpmiddleware

import (
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

func SetRequestIdHeader() gin.HandlerFunc {
	return func(c *gin.Context) {
		uuid := uuid.New().String()
		c.Set("uuid", uuid)
		c.Header("X-Request-Id", uuid)
	}
}
