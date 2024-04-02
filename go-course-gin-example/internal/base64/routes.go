package base64

import "github.com/gin-gonic/gin"

func RegisterRoutes(r *gin.Engine) {
	h := &handler{}

	routesBase64 := r.Group("/base64")
	routesBase64.GET("/decode", h.decode)
	routesBase64.GET("/encode", h.encode)
}
