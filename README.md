# GRPC_ECC

Git clone the package
```
git clone https://github.com/anwaybose/GRPC_ECC.git
```

Install pycryptodome. 
```
pip3 install pycryptodome
pip3 install tinyec
```

Install grpcio-tools. 
```
pip3 install grpcio-tools
```

Build the grpc protocol

```
cd GRPC_ECC/PythonGrpc
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
```

Install the crypto package. 
```cd ../Crypto
pip3 install .
```

