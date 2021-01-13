class SERVER:  # your remote server for test
    HOST = '39.104.80.49'
    USER = 'root'
    KEY_PATH = '/Users/xy/.ssh/id_rsa'


class CDK:
    GO_BINARY = '/Users/xy/go/go1.16beta1/bin/go'
    # local source-code dir to run `go build`
    BUILD_PATH = '/Users/xy/go/CDK/cmd/cdk'
    # build command
    BUILD_CMD = 'cd {} && CGO_ENABLED=0 GOOS=linux GOARCH=amd64 {} build cdk.go'.format(BUILD_PATH,GO_BINARY)
    # binary after build
    BIN_PATH = '/Users/xy/go/CDK/cmd/cdk/cdk'

    # you can keep it unchanged
    REMOTE_HOST_PATH = '/root/cdk-fabric'
    REMOTE_CONTAINER_PATH = '/cdk-fabric'


class K8S:
    # upload cdk to target pod then check command output using kubectl
    TARGET_POD = 'myappnew'
    REMOTE_POD_PATH = '/cdk-fabric'