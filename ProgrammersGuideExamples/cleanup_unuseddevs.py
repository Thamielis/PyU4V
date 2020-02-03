import PyU4V

dellemc_api_conn=PyU4V.U4VConn(username='smc',password='smc',
                               server_ip='xxxxx', verify=None, array_id='000197900111')

dev_filters = {'num_of_front_end_paths': 0,
'private_volumes': False,
'num_of_storage_groups': 0,
'type': 'TDEV'
 }

vollist=dellemc_api_conn.provisioning.get_volume_list(filters=dev_filters)

for i in vollist:
    dellemc_api_conn.provisioning.delete_volume(i)
