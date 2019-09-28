from decimal import *

json_data =  {
    "queryId": "d613aa99-55b5-4386-8444-00000000001d",
    "parentId": None,
    "siblingId": "d613aa99-55b5-4386-8444-00000000001d",
    "childrenId": None,
    "lastModified": "2017-02-22T11:42:27.316+0000",
    "phase": "SUCCESS",
    "startTime": "2017-02-22T11:41:26.774+0000",
    "duration": 2028,
    "transferType": "EXPORT",
    "rowsTransferred": 20,
    "bytesTransferred": 0,
    "compressionRatio": 3.9407232,
    "transferRate": 0,
    "bottleneck": {
      "location": None,
      "node": None
    },
    "configVersion": "ACTIVE",
    "link": {
      "id": "454b0971-9b90-4ffb-b808-f22c042911b8",
      "name": "sdld0997hdp148",
      "version": "ACTIVE",
      "versionId": "a9f30f9a-07bb-4535-aec7-b93b9c62bfc6"
    },
    "fabric": {
      "id": "ae1c02ae-408a-4ced-b3fb-fbfebac77569",
      "name": "test_fabric_01",
      "version": "ACTIVE",
      "versionId": "43a097cc-d60e-42bc-b72b-86e0d0d49ca7",
      "port": 11126,
      "softwareVersion": "02.02.00.00.DEV-28"
    },
    "commPolicy": {
      "id": "bff09854-6bda-433f-8c85-c7749598d198",
      "name": "test_comm_policies_01",
      "version": "ACTIVE",
      "versionId": "07555282-821a-446e-ae5b-1008fcb06d4c",
      "compression": True,
      "encryption": True
    },
    "initiator": {
      "system": {
        "id": "6c66c012-e4f2-474b-a3c9-941dc2637656",
        "name": "sdld0997"
      },
      "connector": {
        "id": "1a2e961e-ad10-4e64-b743-dccd593df86b",
        "name": "sdld0997",
        "version": "ACTIVE",
        "versionId": "1da667cd-820d-4ff9-88ab-b1cd37897b94",
        "softwareName": "tdqg-teradata-connector",
        "softwareVersion": "02.02.00.00.DEV-38"
      },
      "network": {
        "id": "eda38e68-8289-48f3-aa80-a0decbc557f3",
        "name": "test_network_01",
        "version": "ACTIVE",
        "versionId": "83b4957b-d551-4f85-a4e9-d7e5bace95d0"
      },
      "queryText": [
        "INSERT into testuser.temp_t_all_types_simple_x_t_bzip@hdp148 select * from testuser.t_all_types_simple_x--compression_id_2017222_114121_"
      ],
      "username": "TESTUSER",
      "hostId": "1",
      "requestId": "10",
      "sessionId": "3579",
      "queryId": "307190318256663823",
      "totalCpu": 0,
      "metadataPhase": {
        "startTime": "2017-02-22T11:41:26.774+0000",
        "endTime": "2017-02-22T11:41:27.494+0000",
        "duration": 720,
        "totalCpu": 0,
        "bytesTransferred": 0,
        "node": {
          "id": "1fa89e08-3a44-4592-9371-95a9843bf15c",
          "name": "sdld0997.labs.teradata.com"
        }
      },
      "executionPhase": {
        "startTime": "2017-02-22T11:41:27.655+0000",
        "endTime": "2017-02-22T11:41:28.802+0000",
        "duration": 1147,
        "totalCpu": 0,
        "node": {
          "id": "1fa89e08-3a44-4592-9371-95a9843bf15c",
          "name": "sdld0997.labs.teradata.com"
        }
      },
      "dataTransferPhase": {
        "startTime": "2017-02-22T11:41:27.653+0000",
        "endTime": "2017-02-22T11:41:28.265+0000",
        "duration": 612,
        "totalCpu": 0,
        "totalNodes": 1,
        "cpuSkew": 1,
        "highestCpuNode": None,
        "dataSkew": 1,
        "highestDataNode": {
          "id": "1fa89e08-3a44-4592-9371-95a9843bf15c",
          "name": "sdld0997.labs.teradata.com"
        },
        "bytesTransferred": 1687,
        "compressedSize": 1687,
        "decompressedSize": 6648
      },
      "errors": None
    },
    "target": {
      "system": {
        "id": "a41b1d0a-40dc-4939-99ab-03c8d5d182ab",
        "name": "hdp148"
      },
      "connector": {
        "id": "619a905b-2840-4932-b2da-7d1b2c7e3f2b",
        "name": "hdp148",
        "version": "ACTIVE",
        "versionId": "1aab3a4f-e005-4366-83ef-818a1c70c67c",
        "softwareName": "tdqg-presto-connector",
        "softwareVersion": "02.02.00.00.DEV-38"
      },
      "network": {
        "id": "eda38e68-8289-48f3-aa80-a0decbc557f3",
        "name": "test_network_01",
        "version": "ACTIVE",
        "versionId": "83b4957b-d551-4f85-a4e9-d7e5bace95d0"
      },
      "queryText": [
        "SHOW COLUMNS FROM \"testuser\".\"temp_t_all_types_simple_x_t_bzip\"/*d613aa99_55b5_4386_8444_00000000001d_META*/;SELECT t1.query_id, t1.started, t1.analysis_time_ms, t1.distributed_planning_time_ms, t2.completed_splits, t2.split_cpu_time_ms, t2.output_rows, t2.output_bytes, t2.splits, t2.node_id FROM system.runtime.queries t1 INNER JOIN system.runtime.tasks t2 ON t1.query_id = t2.query_id WHERE query LIKE '%d613aa99_55b5_4386_8444_00000000001d_META%' AND t1.state LIKE 'FINISHED'",
        "CREATE TABLE qgremote.DEFAULT.TEMP_d613aa99_55b5_4386_8444_00000000001d_EXEC WITH ( INITIATOR_FORMAT='[{\"t\":1,\"l\":4},{\"t\":1,\"l\":4},{\"t\":2,\"l\":8},{\"t\":47,\"l\":256,\"p\":256},{\"t\":20,\"l\":256,\"p\":256},{\"t\":6,\"l\":16,\"p\":38,\"s\":5},{\"t\":7,\"l\":8},{\"t\":7,\"l\":8}]', CONFIGS='{server=hdp148m1.labs.teradata.com, logfilePath=/var/opt/teradata/tdqg/connector/tdqg-presto-connector/02.02.00.00.DEV-38/logs/, writeTimeout=300000, loaderConnectorName=*.jar, nodeinfo=1fa89e08-3a44-4592-9371-95a9843bf15c, schemaName=default, defaultStringSize=2048, uuid=d613aa99-55b5-4386-8444-00000000001d, linkBufferCount=4, linkBufferSize=73728, connectorPath=/opt/teradata/tdqg/connector/tdqg-presto-connector/02.02.00.00.DEV-38/lib/, security=NONE, prestoWriterCount=8, explainKind=LOGICAL, disablePushdown=False, transformformatting=True, linkHeartbeatInterval=60000, fabricPath=/opt/teradata/tdqg/fabric/02.02.00.00.DEV-28/driver/, linkHandshakeTimeout=30000, remoteConnectorName=*.jar, responseTimeout=1800000, defaultBinarySize=2048, catalogName=hive, port=8090, shmPath=/dev/shm/td_qg_ipc//11126/uds/prod, readTimeout=300000, enableLogging=DEBUG, prestoReaderTaskConcurrency=8, remoteConnectorClassName=com.teradata.querygrid.qgc.presto.remote.PrestoConnectorFactory}') AS (SELECT * FROM \"testuser\".\"temp_t_all_types_simple_x_t_bzip\") WITH NO DATA;INSERT INTO \"testuser\".\"temp_t_all_types_simple_x_t_bzip\" SELECT * FROM qgremote.DEFAULT.TEMP_d613aa99_55b5_4386_8444_00000000001d_EXEC;SELECT t1.query_id, t1.started, t1.analysis_time_ms, t1.distributed_planning_time_ms, t2.completed_splits, t2.split_cpu_time_ms, t2.output_rows, t2.output_bytes, t2.splits, t2.node_id FROM system.runtime.queries t1 INNER JOIN system.runtime.tasks t2 ON t1.query_id = t2.query_id WHERE query LIKE '%INSERT%qgremote.DEFAULT.TEMP_d613aa99_55b5_4386_8444_00000000001d_EXEC%' AND t1.state LIKE 'FINISHED';DROP TABLE IF EXISTS qgremote.DEFAULT.TEMP_d613aa99_55b5_4386_8444_00000000001d_EXEC"
      ],
      "username": "TESTUSER",
      "hostId": "8db6c11a-9614-48e8-91fd-c19b669423d9",
      "requestId": None,
      "sessionId": None,
      "queryId": "20170222_114127_12334_nhayy",
      "totalCpu": 140,
      "metadataPhase": {
        "startTime": "2017-02-22T11:41:26.814+0000",
        "endTime": "2017-02-22T11:41:27.456+0000",
        "duration": 642,
        "totalCpu": 0,
        "bytesTransferred": 0,
        "node": {
          "id": "9d6f8442-deee-41e9-9f50-d0d00d9aec78",
          "name": "hdp148d3.labs.teradata.com"
        }
      },
      "executionPhase": {
        "startTime": "2017-02-22T11:41:27.692+0000",
        "endTime": "2017-02-22T11:41:28.761+0000",
        "duration": 1069,
        "totalCpu": 0,
        "node": {
          "id": "ebc5aba1-7fcb-4ad6-8950-278fe0f4f51a",
          "name": "hdp148d1.labs.teradata.com"
        }
      },
      "dataTransferPhase": {
        "startTime": "2017-02-22T11:41:27.831+0000",
        "endTime": "2017-02-22T11:41:29.319+0000",
        "duration": 1488,
        "totalCpu": 140,
        "totalNodes": 5,
        "cpuSkew": 1.7857143,
        "highestCpuNode": {
          "id": "ea3834a6-4f40-46a2-9993-22e734aaf78b",
          "name": "hdp148d2.labs.teradata.com"
        },
        "dataSkew": 1,
        "highestDataNode": None,
        "bytesTransferred": 0,
        "compressedSize": 1687,
        "decompressedSize": 6648
      },
      "errors": None
    },
    "summaryInfo": {
      "managerId": "107f856e-5c86-442d-95c8-dbaa630e2b1d",
      "indexTime": "2017-02-22T11:41:27.655+0000",
      "summaryDurationSecs": 0.006,
      "summarized": True,
      "complete": True,
      "error": None,
      "lastReceived": {
        "107f856e-5c86-442d-95c8-dbaa630e2b1d": "2017-02-22T11:41:41.976+0000"
      }
    }
  }

print(type(json_data))
getcontext().prec = len(str(json_data['compressionRatio']) ) -1
print(str(json_data['compressionRatio']))
print(Decimal(Decimal(json_data['initiator']['dataTransferPhase']['decompressedSize']) / Decimal(json_data['initiator']['dataTransferPhase']['compressedSize'])))

if str(json_data['compressionRatio']) == str(Decimal(Decimal(json_data['initiator']['dataTransferPhase']['decompressedSize']) / Decimal(json_data['initiator']['dataTransferPhase']['compressedSize']))):
    print("Hello")

if json_data['initiator']['dataTransferPhase']['decompressedSize'] > json_data['initiator']['dataTransferPhase']['compressedSize']:
    print("Chaloo")