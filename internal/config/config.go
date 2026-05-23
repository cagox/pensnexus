package config

import (
	"database/sql"
	"log"
	"os"

	"github.com/cagox/config"
)

var Config *ConfigStruct

type ConfigStruct struct {
	config.ConfigurationStruct

	//Commented items are in config.ConfigurationStruct.
	//SiteName
	//LogPath
	Hosts string
	//Port
	AdminToken        string
	MinimumNameLength int
	MaximumNameLength int
	//EncKey
	Logger  *log.Logger
	LogFile *os.File

	//DatabaseName
	//DatabaseUserName
	//DatabasePassword

	Database *sql.DB //This may change depeneding on db type.
}
