package main

import (
	"fmt"
	"net/http"

	"go-course-gin-example/internal/base64"
	"go-course-gin-example/internal/httpmiddleware"
	"go-course-gin-example/internal/unixtime"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	// Register middleware
	router.Use(httpmiddleware.SetRequestIdHeader())
	router.Use(httpmiddleware.LogRequest())

	// Register routes
	base64.RegisterRoutes(router)
	unixtime.RegisterRoutes(router)

	// Start the server
	srv := http.Server{
		Addr:    fmt.Sprintf(":%d", 3000),
		Handler: router,
	}
	srv.ListenAndServe()

	// router.Run(":3000")
}
