'use strict';

let TRAIN_URL = '/pas/member/train/';
let MEMBER_API = '/pas/api/member/';

$(document).ready(function () {
    $('#members-info').click();
    let btn_group_getfaces = $('.groupBtnGetFaces');

    function check_enable_train_btn(btn_group_getfaces) {
        let count_faces_type_taken = 0;
        for (let i = 0; i < btn_group_getfaces.length; i++) {
            if (btn_group_getfaces[i].hasAttribute('disabled')) {
                count_faces_type_taken += 1;
            }
        }
        if (count_faces_type_taken === 5 ||
            (count_faces_type_taken === 4 && !$('#no_glass_faces')[0].hasAttribute('disabled'))) {
            $('#member_train_warning').html('Have taken enough faces image. Let train now!');
            $('#btn_get_face').attr('disabled', 'disabled');
            $('#btn_train').removeAttr('disabled');
        }
    }

    let btn_train = $('#btn_train');
    if (!btn_train[0].hasAttribute('disabled')) {
        check_enable_train_btn(btn_group_getfaces);
    }

    btn_train.on('click', function () {
        btn_train.button('loading');
        let member_id = $(this).data()['id'];
        let self = this;
        $.ajax({
            type: "get",
            url: TRAIN_URL,
            data: {id: member_id, isTrain: true},
            success: function (data, text) {
                if (data.status === 'success') {
                    toastr.success(data.message, 'Success');
                    $(self).button('disable');
                    // btn_train.button('reset').attr('disabled', 'disabled');
                    $('#btn_train').button('reset');
                    $('#member_train_warning').html('Done!').css('color', 'green');
                    $('#member_threshold').html(data.threshold);
                } else if (data.status === 'warning') {
                    toastr.warning(data.message, 'Warning');
                    $(self).button('reset').attr('disabled', 'disabled');
                } else {
                    toastr.error('Cannot train!', 'Fail');
                    $(self).button('reset').removeAttr('disabled');
                }
            },
            error: function (request, status, error) {
                console.log(error);
                toastr.error(error, 'Fail');
                $(self).button('reset').removeAttr('disabled');
            }
        });
    });

    btn_group_getfaces.on('click', function () {
        // alert(this.id);
        $(this).attr('disabled', 'disabled');
        let member_id = $(this).data()['id'];
        let type = this.id;
        let self = this;
        $.ajax({
            type: "get",
            url: TRAIN_URL,
            data: {id: member_id, isTrain: false, type: type},
            success: function (data, text) {
                if (data.status === 'success') {
                    toastr.success(data.message, 'Success');
                    $(self).parent().find('small').css('display', '');
                    check_enable_train_btn(btn_group_getfaces);
                } else {
                    toastr.error('Cannot take face images!', 'Fail');
                    $(self).removeAttr('disabled');
                    $('#btn_train').attr('disabled', 'disabled');
                }
            },
            error: function (request, status, error) {
                console.log(error);
                toastr.error(error, 'Fail');
            }
        });
    })

    $('#btn_get_more_calculate_money').on('click', function () {
        let member_id = $(this).data()['id'];
        $.ajax({
            type: "get",
            url: '/pas/calculate_hour/',
            data: {id: member_id},
            success: function (data, text) {
                if (data.status === 'success') {
                    toastr.success(data.message, 'Success');
                    console.log(data);
                }
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    });

    $('#btn_change_avatar').on('click', function () {
        $(this).css('display', 'none');
        $('.change_avatar_container').css('display', '');
    });

    $('#upload_avatar').change(function (e) {
        let self = $(this);

        let img_url = URL.createObjectURL(e.target.files[0]);
        $('#img_member_avatar').attr('src', img_url);
        let img = e.target.files[0];
        let data = new FormData();
        data.append('type', 'upload_avatar');
        data.append('id', self.data()['id']);
        data.append('img', img);

        console.log(img);
        $.ajax({
            type: "post",
            contentType: false,
            processData: false,
            url: MEMBER_API,
            data: data,
            success: function (data, text) {
                $('.change_avatar_container').css('display', 'none');
                $('#btn_change_avatar').css('display', '');
                toastr.success(data.message, 'Success');
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    });

    $('#btn_cancel_change_avatar').on('click', function () {
        $('.change_avatar_container').css('display', 'none');
        $('#btn_change_avatar').css('display', '');
    })

});