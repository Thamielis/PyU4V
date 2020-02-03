import PyU4V

dellemc_api_conn=PyU4V.U4VConn(username='smc',password='smc',
                               server_ip='xxx', verify=None, 
                               array_id='000197900111')

sg_list=dellemc_api_conn.provisioning.get_storage_group_list()

for i in sg_list:
    if 'TEMP' in i:
        print (i)
        dellemc_api_conn.provisioning.delete_storage_group((i))
