"""
PHOTOS
======
The manifest for every image on the site. Each entry is:

    (local_path, aspect_ratio, source_url)

  local_path    relative to assets/img/
  aspect_ratio  width / height — this is what lets the gallery justify itself
                in pure CSS, so keep it accurate when you swap a photo:
                    python3 tools/aspect.py assets/img/portraits/07.jpg
  source_url    where the file came from, so the set is reproducible:
                    python3 tools/fetch_photos.py

The source URLs point at Sofia's wfolio CDN — these are her own photographs,
taken from sofiafilatova.wfolio.pro. The site itself serves the LOCAL copies
in assets/img/, so nothing here depends on that subscription staying alive.

TO SWAP A PHOTO
    1. drop the new file into assets/img/<section>/
    2. update its aspect ratio in this file
    3. python3 src/build.py

TO PUT THIS ON TILDA
    Upload your own full-resolution exports through Tilda's image blocks or
    file manager and let Tilda generate the responsive sizes — the copies in
    assets/img/ are capped at 1800px for a fast local preview.
"""

BASE = "assets/img/"

PORTRAITS = [
    ("portraits/01.jpg", 0.812,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/JKwKLu4TAeXIJYogy3iXWDXrENihO44m/1ZKg7gWlBdVN96spbK3e7AkhxSgWgB4i/P_uBAnO9zvMnRknpSgYBrQ.jpg"),
    ("portraits/02.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/3QYbAb1ZqX4FTjUJu-se8m96yJPQ7etQ/ai6abIHLiTBE8jEfUllMHtOfrk11GmLf/2Q3ckEXrPD18GvzvUK9nEg.jpg"),
    ("portraits/03.jpg", 0.771,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/YwyArNUilND7Jga88vSmx7xxLAUM90GT/7juvtQ4PvS3kPtLVxqTJlZAmzhJsqJdE/AT0BrK3_o6OYTM12PssZbA.jpg"),
    ("portraits/04.jpg", 0.764,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/YQ3R5u_cT9Nqw0aw0QKfjysMUYonvCeG/rUrQUaNxOkxpQhmILDXbF24Nw3ABFuy-/k-GUuzadmCj5YNn00NtTog.jpg"),
    ("portraits/05.jpg", 0.758,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/W1-8guPZHfH9PIoSpn3jlFD8ep8cJfcl/Ky7bZgd9v3nrhaV5V4mpIMfxsferdT1y/3LmdtuOAlvBzyb8mqnKT2Q.jpg"),
    ("portraits/06.jpg", 0.764,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/pgMmfaVbnf_rnHpDVgPqLEy-YedEmrBU/kzTXcARbivaqVfgoAuQ4aqIHv6oYcvSp/xUZvr0ygQU5q76Yw6P4fsA.jpg"),
    ("portraits/07.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/cQagxJhAa68dC8SUYx4uSqRBIUfzB7aR/gea89m1gSBbaV7bUGh6CL7gJLa9Cdzvd/gi8DdpJFbmNnJ_2Wm0Kviw.jpg"),
    ("portraits/08.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/dcGLO0-mKM_5uL7rxhaHeuK_4I8zqm11/Vepm-GwV_LE7hfx1oY7Vlf_etl4kli0w/VJl1vSWMCWMr50zALNx_xw.jpg"),
    ("portraits/09.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/HMRCkFLclMCsACHQ7H9YnWsP8k1nbDch/XcV6Z0YXVvSp6nszO-aF78B03wWRKCbn/b-zP5_Eog2LUe6v8cWX8qA.jpg"),
    ("portraits/10.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/ZyUv99x14PcODCTKI30JM8C4vwOInEva/rSvJ2iJV4qc3VkNzS6TfrTsVzoJLF96q/ygFA7nY2DD4bnhZ5-eTRpA.jpg"),
    ("portraits/11.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/BKsVCT5TdQE9k6sEGCTl5o3M3c78t9w1/XZ_y2sdPRe_cov67COP3lE1o3CsrohdT/7WJjsYxOU44hcmRlYs5NqA.jpg"),
    ("portraits/12.jpg", 0.777,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/Hl8jo8kef2Ka9tANhtWrhsfY8m2izlmc/49hnaq2_FcNxSX88T-ZTUZzKl920O1aW/AvM6fscthLZUhBRwEGC5Lw.jpg"),
    ("portraits/13.jpg", 0.661,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/hMnPOGDQ2d2Z-Av0TyrzVi_okE1prbWj/qBc8se9nTfgzd5OSHj5Dm09l0Xndx_HG/pu2EB9DNvNTmdao4JI_18A.jpg"),
    ("portraits/14.jpg", 0.731,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/n6WqY73J9Ii_xvZnME8sajti7a1ewwox/CdFZRVzoP3cnsf0IFCmdSSlPe4LAOuLW/bLzOhwcO5pybQiBFUvRWig.jpg"),
    ("portraits/15.jpg", 0.693,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/jXu0Qe4MN5rO2Vimi73AIqXJgDaRWfEb/DG99CtAoINYlrbqpq_yJyzAwSVddN6j7/l39aCVZL4xesEUglUNGiIQ.jpg"),
    ("portraits/16.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/wD1UukGm8QQ4oFfyV6LWjMAp7JfiRcR5/2NzQzO1nMegUJvafFeUmCb2lojntVDP1/jqWmG6G5xbgkUjS7WBoVKA.jpg"),
    ("portraits/17.jpg", 0.8,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/k-u6CsnhwLuPvUhVH2_7FJU6bbhm2SI8/aJvXMN8qgfEyh5coaxJd1z3Ovr9rP6ZY/v8gyFjVGMPHu8jSRrwcWVg.jpg"),
    ("portraits/18.jpg", 0.8,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/gJ0QhO59fupH9FPetzpIlqLACAcTBGqB/LkmlvYW3hRFw3_sqvPEvyy5o51STE-gH/t7B5lSyiEGN_sjBXJQ46iw.jpg"),
    ("portraits/19.jpg", 0.802,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/ygBrNYu3q4ooANKfRTOLhgNd-_ul62bB/gouL31L_KGi4JNuqBDkfddZgMa9WwHG_/EEsogN_1NNyGZevXZpwhTQ.jpg"),
    ("portraits/20.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/zk77PiiYaRQ6a-ZV9eMNoq_7skI5R0zK/hsCIkM-6Tbf6WsD7vTCD2NAWQxF0PuYq/FIfZ29BDjUz0gkrPZRE1zg.jpg"),
    ("portraits/21.jpg", 0.8,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/XrS4Vo955AmIsD0odEipOfoLOZKlqnXU/bwwqXmKjYYIqmnAjp92EvWzKa5R6Yzcw/vVwkhCkhMnAU-7H-CqIa6g.jpg"),
    ("portraits/22.jpg", 0.8,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/5iRYWmoJiauYEIx5AngGO83YScavpMPh/jcyvrbDYItwZfeG99CUehL2bQPNvB4-i/6D8NWfSvzCWiQYlFoVOtew.jpg"),
    ("portraits/23.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/DLMfQteRarsxbCKqeWyrCPgr3s9FcAW4/tNvIvTTjC_ozRp0KUDC5KOnz2a4OBhpc/fuAByleqlmDHQEUx3amvUQ.jpeg"),
    ("portraits/24.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/iD5NCTWZ21yjiyu8ScNzHHONKBL2AfK0/uhj3h9RqppzFZnj7gu2tVa24Endu3Rxe/Zw_QECa6T6JtD-CFhygYwg.jpeg"),
    ("portraits/25.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/UqNHreSBrrTimAgUV8cZtfteThYjFhNS/Jh-8UIkq6o4QuVZXIFWmlYzf7D9ytYyu/2yHBoCUD_47BJr3Jwbz4Gw.jpg"),
    ("portraits/26.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/OZo83W3nD6LOcDWm-oQzsNkDma1sq3VR/jYbsJZmnqNWVOg1HiCD9awxxMC3DpG81/bMSUd60LisH7-sYBHUUdvw.jpg"),
    ("portraits/27.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/VFKAR-uaf8J-4TkbeKHxFJ9jomtALkh5/CZgFl_v1BEQ7HHUYGdy_oBRm1Nk9oQf4/z1MBBp7GSv00jqIPC2g7OQ.jpg"),
    ("portraits/28.jpg", 0.8,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/AXW9AahGlPs1RUdBFfCbr1MqCI5maNmv/vJS6HvAWXRME4jICUTar4LF1cTovNkJ0/-L_berpwd7e7tRdWfeWlEg.jpg"),
    ("portraits/29.jpg", 1.461,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/jVydhHXNIWE6rw0MNrHKmN3eFC7ZWOR-/PGOSF9irzg80Iwfv30yYjLNc5-j4qcHa/hjJH0dN4B2fafekye7pjBg.jpg"),
    ("portraits/30.jpg", 1.0,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/CdGJqsG3WVqOhOtMKqG_vrxAdb4vBeQp/57hIHkMUJdbHV9bVDW8arThV3WT7rZUV/92bBPoysqC3quoIjCwaAhw.jpeg"),
]

STREET = [
    ("street/01.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/HIK05nJprPZNDSFDQlLmYbiKjIa3Z7bj/w7ArnPRX-O1vXVR5cwVlwmUSmXgBCBTD/2ofq6rpktX5os3dxD8eY_g.jpeg"),
    ("street/02.jpg", 0.663,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/nkGBgnZsgMSrOZ_tngzWApwbQ6a2Wtqc/B53kMJq4QUJi0P-V0hzmBebuyCCfP9J_/oWxTmdUVfI7WlPW8WdL8rQ.jpg"),
    ("street/03.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/bqiNRMs8AKsVn6tes3JEGCNKRuaRliAz/uRZZX9dk7KkEgZmhoOlKyumQp6OtfBvf/J79NbGTjjcNlXMAfjSTBYQ.jpeg"),
    ("street/04.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/wipMWcfx-quPcz9YXOGxTyJTgfz6y-FA/GhqMEoNEy6G07XykWh3EaGeNAeJSj71u/KA8k_XxtKPaow_Fv233uLQ.jpg"),
    ("street/05.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/x_rt15gDTmH-OYA7tGPhfroko_eaNq62/hrOuq4_cmhLGn6OYIVKxT5lWRxZ7hFCL/W5EzzFsVKzVIE78FeceY2Q.jpg"),
    ("street/06.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/qXXLxqwZtidRN2W3IKiixluS4ITNQ8Xv/Se326vb_fee6hvTCDPYrmfdSorStxGfP/c66fVUZV2uqdqpwffjCsFw.jpg"),
    ("street/07.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/rJ7bWpMThr2Y4mNueJlVAIZN4vwkSNTr/fZ1grFhf818ZAw7L0-a5M59nVR02srbs/HdiTh1c8NBj2INLOLzbbWw.jpg"),
    ("street/08.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/sOIBMV25UzqasbmpV3xdbk2zpHlRJQlx/k7L9kTmogGHR6LdA37pp0c8lukGoJdou/T5C2ECvTZrQMUb14RfSB8Q.jpeg"),
    ("street/09.jpg", 0.749,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/mzJ2a4lp_VOPCH6IXlohAKVkRmGktacv/u56Nr8O9BdRXk0mFOKzOKLBFGglRAVB8/2yGDaMW2frl-PdFgAymm-w.jpg"),
    ("street/10.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/oZ3JiWCXdA3uWGHnS8JylvX9u83SZkTb/Xerrb8o6XhwwbQA1i3WENXvkFJ0wDBYI/hXsaJcgPnnClaiJ0i5nhPQ.jpg"),
    ("street/11.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/DltCvJuCiNm4VW1hWu_1ECSBGm2bnKei/HEBJWVYt3Iac4bdnVaPJRJcCSpQ35G1V/le8nIWNv9J0oX4bJuWJTmA.jpg"),
    ("street/12.jpg", 0.786,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/mjWXf8aPMFWfcOh3euNmDHOQ_kU1gAtT/I5SARYu5xrlsw6Qb97jPcgAgvupQ1Ysz/W1gIv5dotXWqH7ZRMtjDEQ.jpg"),
    ("street/13.jpg", 0.865,
     "https://i.wfolio.ru/x/zfNWg0RActCaYvCdP8NS6h3QcKqIOO7I/oVCmpsR2A0_zCBuWQbm7dJYwNQ6ysoqE/kjfuGuabv5LQvkov8c-oaDAq2bEA7uw9/_fwRkfyelJWwxXNqo0oWAtisv2w_0XEP/1WJNXlvjg-tH5k_GxIccyQ.jpg"),
    ("street/14.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/d_aGT8UPIhkQQDhHlddh8pVMbCJQFfGe/rJmJvOEAMdksX5k8g2-sXdYcdoXQEDb0/87PMwZT5s4FjE2C_c_xZUQ.jpg"),
    ("street/15.jpg", 0.664,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/Ef3QL68j5pt_Wut9-G5eOR9Qb01swgy4/ERwEJRPUHhR6lE-xHNqgSCthvpuVLxgC/EdbMqJJ0mqUNbaAmNTqq9g.jpg"),
    ("street/16.jpg", 0.663,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/NOz7LLhE3iVZErljosi9x-u1AI0xKFwJ/zeaB3-_XHh6_--j6Zw0nKVH3yq0pA0EJ/ODbM2sHXgb8NarH960S8Ag.jpg"),
    ("street/17.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/xABiqIz-cfOJhXS2z8M3oWgqf3rDOcOu/fhKh8BaZPQavble6xCDcB5lVz0mL_sEU/AN-XKRmKEEg_nr0qdGOzWw.jpg"),
    ("street/18.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/guFW83EECSqYY8THs8UrGtgP4L7hLV_v/JOpcvZkIXckxaZJRMA5yVGcEDUjiprPi/m4mh3ebnro6Gp0hOLy4r4w.jpeg"),
    ("street/19.jpg", 0.751,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/QRqtoC23T82DqlQY6CA5NiWt1oxLks-V/9u8CRdRklufCIvt-l7-t_SuMHWQ8N0Fk/PKO9a9kVLN70qOWCvKvanw.jpg"),
    ("street/20.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/_I6JTrERru0tPHucIdmOEvletSORfd2z/P8huMmmD77IHmXZlHzlcTgHUsXaYcS0F/U3QBKuo7rTjRf9uyaBRT0g.jpg"),
    ("street/21.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/g7XV6_hPR0-ikUcCRpwWHZshexn_2PQI/OCPId6FXBBW331xLSPYOfYUk7vcf1gl_/PWykQ2EmW6spLB_xgjj51A.jpeg"),
    ("street/22.jpg", 1.768,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/Lfx4GKOmMiHa8aecTnkPpfNHx0Tnn7js/Zq7o0zN0lum09fff3Nvp0XXB5XFS227R/74bzk_okAuCHTUeq-SfNOQ.jpg"),
    ("street/23.jpg", 0.8,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/BX4LHXjwotV0-BAuyEiORem_1GfibwQw/yFRAYeWR87HRKhj3y0QCqtK4XK7D03SO/8IMmP7RMumz5nJ3bLVQ9qg.jpg"),
    ("street/24.jpg", 0.8,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/1Wbqv3ee0v12wd9-RfqFVMd064EyoVuB/ohXUeOeLSku4n_QRciANLXIH7J5AgEoE/oxEiSNmI_qirjL_bGGsPXw.jpg"),
    ("street/25.jpg", 0.764,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/uIqfdqNRgS8JtkwEGRuqF24-zrETFmvn/t_5CdwmaDBGWFx4nnNCPt8FSpgO4ci3_/TgOEWGrufBaGAu2dYq_epA.jpg"),
    ("street/26.jpg", 0.751,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/3Lzhv_r1q6fZpOpsnwFpT4ZQIL-N2nBM/W9pxuc7c_36LdmlmGGKky02jxdbFjPb1/blx-vcx9x-RxNfAN3gUHog.jpg"),
    ("street/27.jpg", 0.658,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/GD6rQMvgjMNQ8bXEL50u4lpjUBK4ADQ9/O0WSsCJYxauq6Co6elXy59vkqfSuXued/b2Jqo8ZmYD6QvnEJ87GSvA.jpg"),
    ("street/28.jpg", 0.8,
     "https://i.wfolio.ru/x/cXPZPmu9lCw5tkRNat7JtyHjrPiZiclN/VJgIrluFLtZWGwzaT5FJ07DuSK__bTQA/OQzsDPC5X0GzdE-7iwSk9F4mjEBwGKS0/5GWLpBOhRjNvfN-E3BhSsE5z9J-wnujY/LWYXBNuRIyLjZt7TWqNG_A.jpg"),
    ("street/29.jpg", 0.562,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/fZrCXl3NfpHr6cgP2aLWsvv1K6WvC7cz/QE4RWdeN-4mHe-zKSaMC6zoGqWrnDskZ/cTFQ6_U0QDGpjI9C3xJ8Qw.jpg"),
    ("street/30.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/ohNjBxAEEVJdHSNmO8RRd4XX79jL1_4I/Z5y9jEJyo7tkBt6ElVjkE76Mle3IF9a9/BQs1LCZXg8VnmPQ8qoKrEA.jpeg"),
]

LOVE = [
    ("love/01.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/w7OarAtd8IKGyQejrRHusROGvfQ1mJ1b/xijxfZiJmPtlbmp8Oin71LQ491bkWpeY/_zMgg4MNT5uhy5u8BxrhDw.jpg"),
    ("love/02.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/tfyS_-ErHAr6NUWVuuQi-tJiT56bgcY8/Bx67T3x99WsMyC4_-vwpGU4yAQI-Ucjb/DHAFBWmbYbZB8USZWQfzhg.jpg"),
    ("love/03.jpg", 1.502,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/z9laB8dQ8_-zClqZIiGicuWl8mz-9xGs/xLVxjzX7VVw_aUfxzvIC-zFBhPDJP0pB/fkQ7_ITXYwFRp-e1tHjEzQ.jpg"),
    ("love/04.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/rOKQ4ENaUUB-RSXDDvnuJRFJ9oMX94xm/iBEzubH3HNhBZG14Yu1EwJ6Y5OffEXAm/m0_JR31NdIA0jvSK_JJvRg.jpg"),
    ("love/05.jpg", 1.502,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/H2tcXad2TGoCnTBs-utmbuc-Kv9iyReH/XPtu_JQQYr7WguuyVCxfNlY3fTxprjm2/gpHw45lxaRzHAp_m8vTF3A.jpg"),
    ("love/06.jpg", 1.502,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/Bb9diiioCuEYod0r-tWIZhCr0hU8f1D9/0X_AYkXWufB3UzVFSA2eZLpiVcxhPKcT/r-BtNvQVPBcOFu5cobi3PA.jpg"),
    ("love/07.jpg", 0.562,
     "https://i.wfolio.ru/x/zRtfFZRdtTOs46O4TlAmB7Xb9GUzndU3/UgFgLXtG2pY5x2bKHSoEXVjMp7HXRFvh/Jof7yzArnT8RBkAYD1v2n8oMX_jn6TJ1/R6-bKMlPJKPtwb-3ylTAmSsX9n9Spius/E8W39YFoLIBXMGjQrsALpg.jpg"),
    ("love/08.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/HVYNl5JAZ6TyEJpqH3fU50iORpm3AUO-/lhWCdUhk7AfEIKbCYFOnLtiOfMBjiD_q/avFMjSotqN1fKfOTNdZrPA.jpg"),
    ("love/09.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/djHXMthUeIP20CcXLOGHwX9aCn0jW87F/5AiGUJq_oVSBvY3UV5wuG_NeiAhQnDaR/fMPGkiT0uQDjkIDYZG1Cmw.jpg"),
    ("love/10.jpg", 1.502,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/dn_yJCvg3haBBN-LZjFwWXAGB0Tgybr3/gZQJ92XjruVmL_U7-CdHQw1OylGn0h0d/NhLFEhq8yQvItVV1vlvCLA.jpg"),
    ("love/11.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/TKPQKj9p4MR5fEZ-Tlr0fmYYiBBAV_rd/kRV3vjT635aG7iBct9Tbm26PuKDapyvX/5C2tO8s7SzqD-0HGY5_vPg.jpg"),
    ("love/12.jpg", 1.502,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/yLT9gNuG5rs7NYv4rAkrPvQBzOBPcUDe/OQD_lLIy4W5tNUYTejKwvFJKpvmINdAM/zGN5MMLpJsBpMO0voGhidg.jpg"),
    ("love/13.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/BInmD3pNtXx62D2IEWmUdQzGwXDZuTPm/lA4zLfLYROMhtVM_r2XkX664A4yAI8LC/IXltYX6OiITH9D3MUpA61w.jpg"),
    ("love/14.jpg", 0.667,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/d7Oa3XXZqxyempvUt69YiVqAM71fE20t/tvsln-s51D181Ml-GgvpftrDJrZ9w_Gy/n5flZ3dQOwJbTjmbfYea2w.jpeg"),
    ("love/15.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/ukeGEilR88U-XTi6Mwag5lMNj76rDNBV/9I7y0_aW7SGsI1YSOxtGWGd3SQNcBzjt/A-W8xIj9UdY0xO3y-fNFKw.jpg"),
    ("love/16.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/HeH5Ogy0cGHDZ6P6XwXZ0nsfhsmyE84v/5647f81Wh5I4dBT9-k7LcnnDB5ETO2y5/ckA-rgIQIxt8AkBkFLIoNw.jpg"),
    ("love/17.jpg", 0.749,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/GX_5JSrm5sf1YLjob1KCOY9hn4a9vjQd/ZcpdOvugvhO23EP5_neA0ojarZjAt7TF/Nn1QGdMxsBG7HBsmFtdoAQ.jpg"),
    ("love/18.jpg", 1.333,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/-vgecgNb4BtSVQ-AzBLxA8_I8ttsxJ6Y/NM13pbD-MjjHH93N1f-ArZnbTZpNv6sv/kGWqOSaQmHeEkVxewF02KA.jpg"),
    ("love/19.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/Onfi_DY11iwAKZZM_7f89eY7asg1u62M/QBY62jhjCFA-6U9m5HLZclEhmGgEuC8S/NfFGixWErKOjojkeF3Rd5g.jpg"),
    ("love/20.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/gr4FXS57pwr7rPNsUs72758aZH_5CEdo/Wqrqmb0DW6gHS3sAs4D87LK3vmrkUz_k/7RIeY4kwpLnWhwpmNsI-sw.jpeg"),
    ("love/21.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/tUqf8jGjVNja69LzphiXFaNYYT39MlMN/Ns4WHWiGBmfM2waM02GExL-D7_dCUP0k/CShi4fyX_z7YTAyi5gOSKw.jpeg"),
    ("love/22.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/w0nkRwG-wMsj_jk7ta_rEZneK5kVo4FV/NqUAnVq0qWAPNEmE7rjc2hAjqE-_i6j8/8PXWmXrTvXx4dWGRoNN0-g.jpeg"),
    ("love/23.jpg", 0.751,
     "https://i.wfolio.ru/x/D48ScH1DA6jxU_uSH-Or-C0cJClpP-QP/lEAL128xEMPGM2o_rKw_kMPHKR9vAJ80/pzC6IU2Yz6jpK6a0fZUrCv5AGFTaKMSC/AQWUJAnuviUgORhKpbLazzlBEE8HTxk3/Bs2Oe8wjKRxM0w_d-h0Djg.jpeg"),
]

# Every photo in one list — used by tools/fetch_photos.py.
ALL_PHOTOS = PORTRAITS + STREET + LOVE + [
    ("sofia.jpg", 1.0,
     "https://i.wfolio.ru/x/1yFBkFi1gsyq0ojRuaj0PymDe_0gU9fY/"
     "5eHBjf9MX9L0kKG74FGkgU2I2fRdHWdo/T9l-KXwr5aIrb36oHgKSqnaI2ZnT5jxj/"
     "EotMgULgkWnK3ZhnUrJC8csdBXzkB_05/2ZaTsmk4eDFX9hDxvWrBspo2rkn7mChC/"
     "oLTC7irbK84.jpg"),
]

# Sofia's own portrait, used in the About block.
SELF_PORTRAIT = BASE + "sofia.jpg"

GALLERIES = {"portraits": PORTRAITS, "street": STREET, "love": LOVE}

# Избранное для сетки на главной. Порядок задан руками: чередование
# вертикальных и горизонтальных кадров нужно, чтобы флексбокс сложил ровные
# ряды примерно по четыре — сумма пропорций ряда выходит около 4.
BEST = [
    "portraits/01.jpg", "love/03.jpg",     "portraits/10.jpg", "street/10.jpg",
    "street/22.jpg",    "love/01.jpg",     "portraits/29.jpg", "love/08.jpg",
    "portraits/05.jpg", "street/01.jpg",   "love/05.jpg",      "portraits/11.jpg",
    "street/03.jpg",    "love/04.jpg",     "portraits/15.jpg", "street/02.jpg",
    "love/06.jpg",      "street/04.jpg",   "portraits/13.jpg", "love/02.jpg",
]

# Один большой кадр-заставка на главной, во всю ширину.
HERO_SHOT = BASE + PORTRAITS[28][0]

# Covers for the three category cards.
COVERS = {
    "portraits": BASE + PORTRAITS[0][0],
    "street":    BASE + STREET[9][0],
    "love":      BASE + LOVE[0][0],
}

# Atmospheric photo beside the contact form, as on the reference.
CONTACT_SHOT = BASE + LOVE[7][0]

# Package illustrations on the price page.
PRICE_SHOTS = {
    "studio":    BASE + PORTRAITS[4][0],
    "walk":      BASE + STREET[5][0],
    "loveStory": BASE + LOVE[8][0],
}
