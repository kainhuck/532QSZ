// package main

// import (
// 	"net/http"

// 	"go.uber.org/zap"
// )

// var logger *zap.Logger
// var sugarLogger *zap.SugaredLogger

// func main() {
// 	InitLogger()
// 	defer logger.Sync()
// 	simpleHttpGetLogger("www.baidu.com")
// 	simpleHttpGetLogger("http://www.baidu.com")

// 	defer sugarLogger.Sync()
// 	simpleHttpGetSugar("www.baidu.com")
// 	simpleHttpGetSugar("http://www.baidu.com")
// }

// func InitLogger() {
// 	logger, _ = zap.NewProduction()
// 	sugarLogger = logger.Sugar()
// }

// func simpleHttpGetLogger(url string) {
// 	resp, err := http.Get(url)
// 	if err != nil {
// 		logger.Error("Error fetching url..", 
// 			zap.String("url", url),
// 			zap.Error(err))
// 	} else {
// 		logger.Info("Success..",
// 			zap.String("statusCode", resp.Status),
// 			zap.String("url", url))
// 		resp.Body.Close()
// 	}
// }

// func simpleHttpGetSugar(url string) {
// 	resp, err := http.Get(url)
// 	if err != nil {
// 		logger.Error("Error fetching url..", 
// 			zap.String("url", url),
// 			zap.Error(err))
// 	} else {
// 		logger.Info("Success..",
// 			zap.String("statusCode", resp.Status),
// 			zap.String("url", url))
// 		resp.Body.Close()
// 	}
// }