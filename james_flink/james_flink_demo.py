# ******************
# FLINK BATCH QUERY
# ******************
from pyflink.dataset import ExecutionEnvironment
from pyflink.table import BatchTableEnvironment, TableConfig, DataTypes
from pyflink.table.descriptors import FileSystem, OldCsv, Schema

env = ExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(env, t_config)

src_file_path = '/home/james/workspace/JamesFlink/src/main/resources/data/hello.txt'
sink_file_path = 'data/hello.out'

t_env.connect(FileSystem().path(src_file_path)).with_format(
    OldCsv().line_delimiter(' ').field('word', DataTypes.STRING())).with_schema(
    Schema().field('word', DataTypes.STRING())).register_table_source('jamesSource')

t_env.connect(FileSystem().path(sink_file_path)).with_format(
    OldCsv().field_delimiter('\t').field('word', DataTypes.STRING()).field('count', DataTypes.BIGINT())).with_schema(
    Schema().field('word', DataTypes.STRING()).field('count', DataTypes.BIGINT())).register_table_sink('jamesSink')

# t_env.scan('mySource').group_by('word').select('word, count(1)').insert_into('mySink')
# t_env.scan('mySource').group_by('word').select('word, count(1)').print_schema()
t_env.scan('jamesSource').group_by('word').select('word, count(1)').insert_into('jamesSink')

t_env.execute("python_job")
