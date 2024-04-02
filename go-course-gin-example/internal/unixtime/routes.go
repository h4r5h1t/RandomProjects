package unixtime

import "github.com/gin-gonic/gin"

func RegisterRoutes(r *gin.Engine) {
	h := &handler{}

	routesUnixtime := r.Group("/unixtime")
	routesUnixtime.GET("/:timestamp", h.toHuman)
}
