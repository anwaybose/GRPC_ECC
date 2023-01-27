# GRPC_ECC


Install pycryptodome
`pip install pycryptodome`

Install grpcio-tools
`pip3 install grpcio-tools`

`cd GRPC_ECC/PythonGrpc`
`python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto`

Install the crypto package
`cd ../Crypto`
`pip install .`

