package httpmiddleware

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func LogRequest() gin.HandlerFunc {
	return func(c *gin.Context) {
		uuid, _ := c.Get("uuid")
		fmt.Printf("The request with uuid %s is started \n", uuid.(string))
		c.Next()
		fmt.Printf("The request with uuid %s is finished \n", uuid.(string))
	}
}
