# psychic-parakeet
A basid FastMCP client and server.

## Server
```sh
source /home/ubuntu/py/github.com/seblkma/psychic-parakeet/.venv/bin/activate
ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet$ source /home/ubuntu/py/github.com/seblkma/psychic-parakeet/.venv/bin/activate
(psychic-parakeet) ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet$ cd basic
(psychic-parakeet) ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet/basic$ uv run server.py 


            ╭──────────────────────────────────────────────────────────────────────────────╮             
            │                                                                              │             
            │                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │             
            │                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │             
            │                                                                              │             
            │                                FastMCP 2.13.1                                │             
            │                                                                              │             
            │                                                                              │             
            │                   🖥  Server name: Document Assistant                         │             
            │                                                                              │             
            │                   📦 Transport:   SSE                                        │             
            │                   🔗 Server URL:  http://0.0.0.0:8000/sse                    │             
            │                                                                              │             
            │                   📚 Docs:        https://gofastmcp.com                      │             
            │                   🚀 Hosting:     https://fastmcp.cloud                      │             
            │                                                                              │             
            ╰──────────────────────────────────────────────────────────────────────────────╯             


[11/21/25 03:27:12] INFO     Starting MCP server 'Document Assistant' with transport 'sse' server.py:2055
                             on http://0.0.0.0:8000/sse                                                  
INFO:     Started server process [126917]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## Client
```sh
ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet$ source /home/ubuntu/py/github.com/seblkma/psychic-parakeet/.venv/bin/activate
(psychic-parakeet) ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet$ cd basic
(psychic-parakeet) ubuntu@ubuntu:~/py/github.com/seblkma/psychic-parakeet/basic$ uv run client.py 
Client connected: True
Available tools: [Tool(name='edit_file', title=None, description='Asynchronously appends a line of text to the end of a file.', inputSchema={'properties': {'filename': {'description': 'Path to the target file', 'maxLength': 255, 'minLength': 1, 'type': 'string'}, 'line': {'description': 'Text content to append to the file', 'minLength': 1, 'type': 'string'}, 'second_line': {'default': '', 'description': 'Optional second line to append to the file', 'minLength': 1, 'type': 'string'}}, 'required': ['filename', 'line'], 'type': 'object'}, outputSchema=None, icons=None, annotations=None, meta={'_fastmcp': {'tags': []}})]
[11/21/25 03:27:33] INFO     Received INFO from server: {'msg': 'Analyzing 42 data points', logging.py:44
                             'extra': None}                                                              
Greet result: CallToolResult(content=[], structured_content=None, meta=None, data=None, is_error=False)
Client connected: False
```