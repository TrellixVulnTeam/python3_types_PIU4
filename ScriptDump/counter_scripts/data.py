
built_in_types = [

    # Super-special typing primitives.
    'Any',
    'Callable',
    'ClassVar',
    'Final',
    'ForwardRef',
    'Generic',
    'Literal',
    'Optional',
    'Protocol',
    'Tuple',
    'Type',
    'TypeVar',
    'Union',

    # ABCs (from collections.abc).
    'AbstractSet',  # collections.abc.Set.
    'ByteString',
    'Container',
    'ContextManager',
    'Hashable',
    'ItemsView',
    'Iterable',
    'Iterator',
    'KeysView',
    'Mapping',
    'MappingView',
    'MutableMapping',
    'MutableSequence',
    'MutableSet',
    'Sequence',
    'Sized',
    'ValuesView',
    'Awaitable',
    'AsyncIterator',
    'AsyncIterable',
    'Coroutine',
    'Collection',
    'AsyncGenerator',
    'AsyncContextManager',

    # Structural checks, a.k.a. protocols.
    'Reversible',
    'SupportsAbs',
    'SupportsBytes',
    'SupportsComplex',
    'SupportsFloat',
    'SupportsIndex',
    'SupportsInt',
    'SupportsRound',

    # Concrete collection types.
    'ChainMap',
    'Counter',
    'Deque',
    'Dict',
    'DefaultDict',
    'List',
    'OrderedDict',
    'Set',
    'FrozenSet',
    'NamedTuple',  # Not really a type.
    'TypedDict',  # Not really a type.
    'Generator',

    # One-off things.
    'AnyStr',
    'cast',
    'final',
    'get_args',
    'get_origin',
    'get_type_hints',
    'NewType',
    'no_type_check',
    'no_type_check_decorator',
    'NoReturn',
    'overload',
    'runtime_checkable',
    'Text',
    'TYPE_CHECKING',

    '''
    # types.Type Types arising in Python interpreter                                                                                                                                                                                                                                                                                          
    'BaseException',                                                                                                                                                            
    'FunctionType',                                                                                                                                                                    
    'LambdaType',                                                                                                                                                                      
    'GeneratorType',                                                                                                                                                                 
    'CoroutineType',                                                                                                                                                                  
    'AsyncGeneratorType',                                                                                                                                                             
    'CodeType',                                                                                                                                                                        
    'CellType',                                                                                                                                                                        
    'MethodType',                                                                                                                                                                      
    'BuiltinFunctionType',                                                                                                                                                             
    'BuiltinMethodType',                                                                                                                                                               
    'WrapperDescriptorType',                                                                                                                                                           
    'MethodWrapperType',                                                                                                                                                               
    'MethodDescriptorType',                                                                                                                                                            
    'ClassMethodDescriptorType',                                                                                                                                                       
    'ModuleType',                                                                                                                                                                      
    'TracebackType',                                                                                                                                                                   
    'FrameType',                                                                                                                                                                   
    'GetSetDescriptorType',                                                                                                                                                            
    'MemberDescriptorType',                                                                                                                                                            
    'MappingProxyType',                                                                                                                                                                
    'SimpleNamespace',                                                                                                                                                                 
    'DynamicClassAttribute',
    '''    

    #re and text modules from typing
    'IO',
    'TextIO',
    'BinaryIO',
    'Pattern',
    'Match',
    #'AsyncObservable',
    'InitVar',
    'AnyType'
    #'ndarray',
    #'callable',
    #'datetime',
    #'Exception',
    #'array',
    #'Path',
    #'Logger' 
]
