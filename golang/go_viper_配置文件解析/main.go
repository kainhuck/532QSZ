package main

import (
	"fmt"
	"os"

	"github.com/spf13/viper"
)

type config struct {
	v *viper.Viper
}

func main() {
	c := &config{}

	yamlConfig, err := UnmshalStruct(c)
	if err != nil {
		panic(err)
	}

	fmt.Println(yamlConfig.TimeStamp)
}

// 读取yaml配置文件
func LoadConfigFromYaml(c *config) error {
	c.v = viper.New()

	// 1.设置配置文件名: 默认名称为`config` 见`viper.New()`方法
	c.v.SetConfigName("config")
	// 2.设置配置文件类型支持:  JSON, TOML, YAML, HCL, envfile and Java properties config files
	c.v.SetConfigType("yaml")
	// 3.设置配置文件存放的目录,可以设置多个目录,viper将会从这些目录下寻找指定的配置文件,如果没有设置会在程序执行的目录寻找配置文件
	c.v.AddConfigPath("./")

	// 或者使用下面这个函数直接读取指定路径的配置文件
	// c.v.SetConfigFile("./config.yaml")

	// 设置好配置文件后需要读取
	if err := c.v.ReadInConfig(); err != nil {
		return err
	}

	return nil
}

// 从IO中读取配置文件
func LoadConfigFromIO(c *config) error {
	c.v = viper.New()
	f, err := os.Open("./config.yaml")
	if err != nil {
		return fmt.Errorf("文件打开出错: %s", err)
	}

	defer f.Close()

	// 指定配置文件类型
	c.v.SetConfigType("yaml")
	c.v.ReadConfig(f)

	return nil
}

func GetValues() {
	c := &config{}

	if err := LoadConfigFromYaml(c); err != nil {
		panic(err)
	}

	// 所有方法 key 都不区分大小写

	// Get方法可以自动判断map slice bool string int 类型,
	// 不能对string类型进行细分,比如`TimeStamp`,只要被加引号都认为是string
	info := c.v.Get("Information")
	fmt.Printf("%T, %v \n", info, info)

	// GetStringMap
	info = c.v.GetStringMap("information")
	fmt.Printf("%T, %v\n", info, info)

	// GetTime
	t := c.v.GetTime("TimeStamp")
	fmt.Printf("%T %v\n", t, t)

	// ...
}

type information struct {
	Name   string
	Age    int
	Alise  []string
	Image  string
	Public bool
}

type favorite struct {
	Sport       []string
	Music       []string
	LuckyNumber int
}

type YamlConfig struct {
	TimeStamp   string
	Author      string
	PassWd      string
	Information information
	Favorite    favorite
}

// 将配置文件反序列化为结构体
func UnmshalStruct(c *config) (*YamlConfig, error) {
	err := LoadConfigFromYaml(c)
	if err != nil {
		return nil, err
	}

	var cf YamlConfig
	err = c.v.Unmarshal(&cf)

	return &cf, err
}
