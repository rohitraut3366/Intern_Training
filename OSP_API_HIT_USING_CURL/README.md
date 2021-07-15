# OSP-GLANCE_API

## STEPS:
   * Issue Token
     * Download RC file
     * source rc file
     * run cmd: `openstack token issue`
   * visit: https://docs.openstack.org/api-ref/image/v2/index.html
     
     
 

1. List IMAGES
```
   End-Point: http://IP/v2/images
   Method: GET
   CURL:   curl  -X GET -H "X-AUTH_TOKEN: gAAAAABg7s0Bcp2MdxjGTfWrhjnn_wBodKp8esrmiXKMEkh5wwZS00ziRPOrGZrm_mcYH23Vak9QkeiW1dXtjs_04JYJB5Rf96QmGL45Y9Ea7p0A3HQBudmf3wKMPYvjF5Wd8tQKOGxR7Ii__RrR9Q5afkHq3SqZ0xrATlq4NKkIVt32o5wxsOE"  http://10.0.78.69/image/v2/images

   Requests:
       {}
   Response:
       {
          "images": [{
            "architecture": "x86_64",
            "name": "centos-cmd-test2",
            "disk_format": null,
            "container_format": null,
            "visibility": "public",
            "size": null,
            "virtual_size": null,
            "status": "queued",
            "checksum": null,
            "protected": false,
            "min_ram": 0,
            "min_disk": 0,
            "owner": "451b3702cafc46be87c6ed34104e7943",
            "os_hidden": false,
            "os_hash_algo": null,
            "os_hash_value": null,
            "id": "66d7043a-bf24-48a4-9cd7-f4cc7403ffa9",
            "created_at": "2021-07-14T05:38:11Z",
            "updated_at": "2021-07-14T05:38:11Z",
            "tags": [],
            "self": "/v2/images/66d7043a-bf24-48a4-9cd7-f4cc7403ffa9",
            "file": "/v2/images/66d7043a-bf24-48a4-9cd7-f4cc7403ffa9/file",
            "schema": "/v2/schemas/image"
          }, {
            "architecture": "x86_64",
            "name": "centos-cmd",
            "disk_format": null,
            "container_format": null,
            "visibility": "public",
            "size": null,
            "virtual_size": null,
            "status": "queued",
            "checksum": null,
            "protected": false,
            "min_ram": 0,
            "min_disk": 0,
            "owner": "451b3702cafc46be87c6ed34104e7943",
            "os_hidden": false,
            "os_hash_algo": null,
            "os_hash_value": null,
            "id": "cb337799-44e9-400a-9a1e-88276f864cb7",
            "created_at": "2021-07-14T04:41:17Z",
            "updated_at": "2021-07-14T04:41:17Z",
            "tags": [],
            "self": "/v2/images/cb337799-44e9-400a-9a1e-88276f864cb7",
            "file": "/v2/images/cb337799-44e9-400a-9a1e-88276f864cb7/file",
            "schema": "/v2/schemas/image"
          }, {
            "name": "centos",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "shared",
            "size": 283838816,
            "virtual_size": null,
            "status": "active",
            "checksum": "6a5cb01dbd41b3ee6b9ae735480ff375",
            "protected": false,
            "min_ram": 0,
            "min_disk": 0,
            "owner": "451b3702cafc46be87c6ed34104e7943",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "662719b912bccccc30338a8d84022d04123eb658c0c52e76f813a2b953745344f21d3f8a7e295e3f7b4734692d8fbc23fc8010f68f2826112aa9f6fc5b2b6b99",
            "id": "13d88679-8f83-4d46-bddb-fa3a1cbd14dc",
            "created_at": "2021-07-13T19:54:07Z",
            "updated_at": "2021-07-13T19:54:08Z",
            "tags": [],
            "self": "/v2/images/13d88679-8f83-4d46-bddb-fa3a1cbd14dc",
            "file": "/v2/images/13d88679-8f83-4d46-bddb-fa3a1cbd14dc/file",
            "schema": "/v2/schemas/image"
          }, {
            "hw_rng_model": "virtio",
            "owner_specified.openstack.md5": "",
            "owner_specified.openstack.object": "images/cirros-0.5.2-x86_64-disk",
            "owner_specified.openstack.sha256": "",
            "name": "cirros-0.5.2-x86_64-disk",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 16300544,
            "virtual_size": 117440512,
            "status": "active",
            "checksum": "b874c39491a2377b8490f5f1e89761a4",
            "protected": false,
            "min_ram": 0,
            "min_disk": 0,
            "owner": "451b3702cafc46be87c6ed34104e7943",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "6b813aa46bb90b4da216a4d19376593fa3f4fc7e617f03a92b7fe11e9a3981cbe8f0959dbebe36225e5f53dc4492341a4863cac4ed1ee0909f3fc78ef9c3e869",
            "id": "6caf7a3f-feb9-4fb1-afb2-993c1ef019e6",
            "created_at": "2021-07-13T07:23:18Z",
            "updated_at": "2021-07-13T07:23:19Z",
            "tags": [],
            "self": "/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6",
            "file": "/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6/file",
            "schema": "/v2/schemas/image"
          }],
          "first": "/v2/images",
          "schema": "/v2/schemas/images"
        }
 ```


2. Show image
```
   End-Point: http://IP/v2/images/{image_id}
   Method: GET
   
   CURL:   curl -H "X-AUTH_TOKEN: gAAAAABg7tta4mdWOXtEtEudACBjwnFlvEA2tqgifzX5n6jRLmaCemqqIQR9t4XqDpGaClVKuuHkgkC8eMN1LOoR1Pf9YIviyj3eeD0FjLZtEJYik0K6FVAEqnp_2-MClNB-MaOmsS3SabcDLG612xWqNgOJby2tLeWsB1y1EdG8z3NelX3LXvE"  http://10.0.78.69/image/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6
   
   Requests:
   
       {}
       
   Response:
    {
       "hw_rng_model":"virtio",
       "owner_specified.openstack.md5":"",
       "owner_specified.openstack.sha256":"",
       "owner_specified.openstack.object":"images/cirros-0.5.2-x86_64-disk",
       "name":"cirros-0.5.2-x86_64-disk",
       "disk_format":"qcow2",
       "container_format":"bare",
       "visibility":"public",
       "size":16300544,
       "virtual_size":117440512,
       "status":"active",
       "checksum":"b874c39491a2377b8490f5f1e89761a4",
       "protected":false,
       "min_ram":0,
       "min_disk":0,
       "owner":"451b3702cafc46be87c6ed34104e7943",
       "os_hidden":false,
       "os_hash_algo":"sha512",
       "os_hash_value":"6b813aa46bb90b4da216a4d19376593fa3f4fc7e617f03a92b7fe11e9a3981cbe8f0959dbebe36225e5f53dc4492341a4863cac4ed1ee0909f3fc78ef9c3e869",
       "id":"6caf7a3f-feb9-4fb1-afb2-993c1ef019e6",
       "created_at":"2021-07-13T07:23:18Z",
       "updated_at":"2021-07-13T07:23:19Z",
       "tags":[

       ],
       "self":"/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6",
       "file":"/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6/file",
       "schema":"/v2/schemas/image"
    }
```

3.  Show tasks associated with image
```
   End-Point: http://IP/v2/images/{image_id}
   Method: GET
 
   CURL:   curl -H "X-AUTH_TOKEN: gAAAAABg7tta4mdWOXtEtEudACBjwnFlvEA2tqgifzX5n6jRLmaCemqqIQR9t4XqDpGaClVKuuHkgkC8eMN1LOoR1Pf9YIviyj3eeD0FjLZtEJYik0K6FVAEqnp_2-MClNB-MaOmsS3NgOJby2tLeWsB1y1EdG8z3NelX3LXvE"  http://10.0.78.69/image/v2/images/6caf7a3f-feb9-4fb1-afb2-993c1ef019e6/tasks

   Requests:
       {}
   Response:
      {"tasks": []}
```

4.  Create Image
```
   End-Point: http://IP/v2/image
   Method: POST
   
   CURL:   curl -X POST -H "X-AUTH_TOKEN: gAAAAABg7u5lLgCGyQEj9ytEaBtKCLjFJZI3yGu7q_k7Txz312J26IVIaL0nMQ5Rv_Yd-bIE3ZTJ9IIEM0yA3wTmhhHaxmYnijSZjCD4Hh6ehdsII1If8kwBx8DUNzQ7ZsqpflqQ-sI68IqVs11g2ptR-JhUd427FVoXbK39f4b7IUYTKUhUt78" -H "content-type: application/json" -d '{"disk_format": "qcow2", "min_disk": 2, "min_ram": 1, "name": "centos"}'  http://10.0.78.69/image/v2/images

   Requests:
       {{"name": "Centos 7-Patch-Name", "disk_format": "qcow2", "container_format": null, "visibility": "shared", "size": null, "virtual_size": null, "status": "queued", "checksum": null, "protected": false, "min_ram": 1, "min_disk": 2, "owner": "451b3702cafc46be87c6ed34104e7943", "os_hidden": false, "os_hash_algo": null, "os_hash_value": null, "id": "f1fa3214-a3d0-4f78-b8c0-7674ff5f4538", "created_at": "2021-07-14T14:06:41Z", "updated_at": "2021-07-14T18:38:09Z", "tags": [], "self": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538", "file": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538/file", "schema": "/v2/schemas/image"}[centos
          "disk_format" : "qcow2",
          "min_disk": 2,
          "min_ram": 1,
          "name": "centos7"
       }
   Response:
        {
          "name": "centos",
          "disk_format": "qcow2",
          "container_format": null,
          "visibility": "shared",
          "size": null,
          "virtual_size": null,
          "status": "queued",
          "checksum": null,
          "protected": false,
          "min_ram": 1,
          "min_disk": 2,
          "owner": "451b3702cafc46be87c6ed34104e7943",
          "os_hidden": false,
          "os_hash_algo": null,
          "os_hash_value": null,
          "id": "f1fa3214-a3d0-4f78-b8c0-7674ff5f4538",
          "created_at": "2021-07-14T14:06:41Z",
          "updated_at": "2021-07-14T14:06:41Z",
          "tags": [],
          "self"{"name": "Centos 7-Patch-Name", "disk_format": "qcow2", "container_format": null, "visibility": "shared", "size": null, "virtual_size": null, "status": "queued", "checksum": null, "protected": false, "min_ram": 1, "min_disk": 2, "owner": "451b3702cafc46be87c6ed34104e7943", "os_hidden": false, "os_hash_algo": null, "os_hash_value": null, "id": "f1fa3214-a3d0-4f78-b8c0-7674ff5f4538", "created_at": "2021-07-14T14:06:41Z", "updated_at": "2021-07-14T18:38:09Z", "tags": [], "self": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538", "file": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538/file", "schema": "/v2/schemas/image"}[centos: "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538",
          "file": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538/file",
          "schema": "/v2/schemas/image"
         }
```
5. Update Image
```
   End-Point: http://IP/image/v2/images/{image_id}
   Method: PATCH
   
   CURL: curl -X PATCH -H "content-type: application/openstack-images-v2.1-json-patch" -H "X-AUTH-TOKEN: gAAAAABg7y1JwHj3r9TNcURhW3crv1RsFgM2_J8wD_fcDnosT-ZcRGoPLOtTgKLDWlHfSevyc9k6DjC_yuqconOQ6V4ThwJ0YD_7vBOYjOMdXAw7qo9ysE_mqfXkqHq7iIGjY_KT0vtU3YU5uHCGtLGgVpliNT4Qku252iNQ72ow0-cg" -d '[{"op": "replace", "path": "/name", "value": "Centos 7-Patch-Name"}]' http://10.0.78.69/image/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538

   Requests:
      [
         {
            "op": "replace",
            "path": "/name",
            "value": "Centos 7-Patch-Name"
         }
      ]
   Response:
      {
            "name": "Centos 7-Patch-Name",
            "disk_format": "qcow2",
            "container_format": null,
            "visibility": "shared",
            "size": null,
            "virtual_size": null,
            "status": "queued",
            "checksum": null,
            "protected": false,
            "min_ram": 1,
            "min_disk": 2,
            "owner": "451b3702cafc46be87c6ed34104e7943",
            "os_hidden": false,
            "os_hash_algo": null,
            "os_hash_value": null,
            "id": "f1fa3214-a3d0-4f78-b8c0-7674ff5f4538",
            "created_at": "2021-07-14T14:06:41Z",
            "updated_at": "2021-07-14T18:38:09Z",
            "tags": [],
            "self": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538",
            "file": "/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538/file",
            "schema": "/v2/schemas/image"
      }
```

6. DELETE Image
### Preconditions
    * You can delete an image in any status except deleted.
    * The protected attribute of the image cannot be true.
    * You have permission to perform image deletion under the configured image deletion policy.
 ```
   End-Point: http://IP/image/v2/images/{image_id}
   Method: DELETE
   
   CURL:  curl -X DELETE -H "X-AUTH_TOKEN: gAAAAABg7zO01wYMs2pyxBgr0zfsv2emQpglwdyB6udcr0c_PJ1HeMCQdjUSnhmf2wEzLjGsN3B0IuC9kIg0eLgj1FqcsQl86YEGlbKJdQ7EhNj9cq3D_rrfGQ6Le55GtmexrWwh5UB8XV5xw8EoGbWL8Pz8Z_msqtvxh1Kb7We9K21Qg5JRUxBg"  http://10.0.78.69/image/v2/images/f1fa3214-a3d0-4f78-b8c0-7674ff5f4538

   Request: NULL
   Response: NULL
 
 ```
 
 7. PUT Image
```
 End-Point API: http://IP/image/v2/images/{image_id}/tags/{tag}
 Method: PUT
 
 CURL:      curl -X PUT -H "X-AUTH_TOKEN: gAAAAABg79auA-Pka-bMyB2vpoMZ95_OHyaJZDEUgXJM4Gd3oBUcSwF9h3lWLHgREMc48ZDBmpwtUZ50RaN01dOra22m9L-KHhHTNk7RR_HO4DJYXxRJquEcDTiuGg94pUzp_OmP7qWLgD02tQpWnAJa-X0VbPKQdPpvdpK2jaiSU6fux4iwwPg"  http://10.0.78.69/image/v2/images/13d88679-8f83-4d46-bddb-fa3a1cbd14dc/tags/tag1
   Request: {}
   Response: {}
```
