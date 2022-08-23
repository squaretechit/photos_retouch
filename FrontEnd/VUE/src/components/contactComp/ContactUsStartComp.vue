<script>
    import {ref} from "vue";
    import {getAPI,baseURL} from "@/axios-api";
    export default {
        data: () => ({
            VFullName: ref(''),
            VEmail: ref(''),
            VPhone: ref(''),
            VComment: ref(''),
            VSuccessMessage: ref(''),
            VSendToServer: false,
            VErrors: ref({})
        }),
        methods: {
            // Send Data To Server
            SubmitFormToServer() {
                getAPI.post('/contact/',{
                    'name': this.VFullName,
                    'email': this.VEmail,
                    'phone_number': this.VPhone,
                    'comment': this.VComment
                })
                .then(response => {
                    this.VSuccessMessage = response.data['message'];
                    this.VFullName = '';
                    this.VEmail = '';
                    this.VPhone = '';
                    this.VComment = '';
                    this.VSendToServer = true;
                }).catch(err => console.log(err.message))
            },
            // Check Valid Email
            validEmail(email) {
                let re =
                    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },
            // Check Valid Phone Number
            validNumber(number) {
                let re = /^([0-9]+)$/;
                return re.test(number);
            },
            // Submit The Form
            SubmitForm() {
                this.VErrors = {};
                if (!this.VFullName) {
                    this.VErrors['FullName'] = 'Name Required.';
                }
                if (!this.VEmail) {
                    this.VErrors['Email'] = 'Email Required.';
                } else if (!this.validEmail(this.VEmail)) {
                    this.VErrors['Email'] = 'Please use a valid Email.';
                }
                if (!this.VPhone) {
                    this.VErrors['Phone'] = 'Phone Number Required.';
                } else if (!this.validNumber(this.VPhone)) {
                    this.VErrors['Phone'] = 'Please use a valid Phone number.';
                }
                if (!this.VComment) {
                    this.VErrors['Comment'] = 'Comment Required.';
                }
                if (!this.VErrors['FullName'] && !this.VErrors['Email'] && !this.VErrors['Phone'] && !this.VErrors[
                        'Comment']) {
                    this.SubmitFormToServer();
                }
            }
        }
    }
</script>

<template>
    <section class="contact-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/assets/images/ContactComp/ContactUsStartComp/contact-icon-1.png" alt="Icons">
                        </div>
                        <p><span>Address</span></p>
                        <p>31 Somestreet Cambridge, CB4 3AA, Russia</p>
                        <p class="ph-number"><i class="fa fa-microphone"></i> 02771 57 00 51</p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/assets/images/ContactComp/ContactUsStartComp/contact-icon-2.png" alt="Icons">
                        </div>
                        <p><span>Email Address</span></p>
                        <p>help@gmail.com</p>
                        <p>help@agopa.com</p>
                        <p class="ph-number"><i class="fa fa-microphone"></i> 02771 57 00 51</p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/assets/images/ContactComp/ContactUsStartComp/contact-icon-3.png" alt="Icons">
                        </div>
                        <p><span>Offie phone number</span></p>
                        <p>+011 05 2232161</p>
                        <p>+011 1120001</p>
                        <p class="ph-number"><i class="fa fa-microphone"></i> 02771 57 00 51</p>
                    </div>
                </div>
            </div>
            <div class="row contact-form-row justify-content-center">
                <div class="col-lg-8">
                    <form @submit.prevent="SubmitForm" novalidate>
                        <div class="row">
                            <div class="col-sm-12">
                                <p class="text-center success-message" v-if="VSuccessMessage">{{VSuccessMessage}}</p>
                            </div>
                            <div class="col-sm-12">
                                <input v-model="VFullName" :class="{inputError: VErrors.FullName}" class="form-control"
                                    type="text" placeholder="Your name">
                                <p v-if="VErrors.FullName" class="errors">{{ VErrors.FullName }}</p>
                            </div>
                            <div class="col-sm-6">
                                <input v-model="VEmail" :class="{inputError: VErrors.Email}" class="form-control"
                                    type="email" placeholder="Valid email">
                                <p v-if="VErrors.Email" class="errors">{{ VErrors.Email }}</p>
                            </div>
                            <div class="col-sm-6">
                                <input v-model="VPhone" :class="{inputError: VErrors.Phone}" class="form-control"
                                    type="text" placeholder="Phone number with Country Code">
                                <p v-if="VErrors.Phone" class="errors">{{ VErrors.Phone }}</p>
                            </div>
                            <div class="col-sm-12">
                                <textarea v-model="VComment" :class="{inputError: VErrors.Comment}" class="form-control"
                                    placeholder="Your comment"></textarea>
                                <p v-if="VErrors.Comment" class="errors">{{ VErrors.Comment }}</p>
                            </div>
                            <div class="col-sm-12">
                                <button class="btn btn-primary my-btn" type="submit">SUBMIT</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
    .inputError {
        margin-bottom: 0 !important;
    }

    .success-message {
        background: #2791BF;
        color: #fff;
        padding: 10px;
        border-radius: 3px;
        margin-bottom: 20px;
    }

    .contact-area {
        padding: 0 0 100px;
        margin-top: 300px;
        -webkit-box-shadow: -5px 0px 22px 0px rgba(205, 205, 205, 0.35);
        -moz-box-shadow: -5px 0px 22px 0px rgba(205, 205, 205, 0.35);
        box-shadow: -5px 0px 22px 0px rgba(205, 205, 205, 0.35);
    }

    .information-box {
        text-align: center;
        background: #ffffff;
        padding: 120px 70px 70px;
        position: relative;
        margin-top: -135px;
        margin-bottom: 30px;
        -webkit-box-shadow: -5px 0px 37px 0px rgba(243, 216, 255, 0.35);
        -moz-box-shadow: -5px 0px 37px 0px rgba(243, 216, 255, 0.35);
        box-shadow: -5px 0px 37px 0px rgba(243, 216, 255, 0.35);
    }

    .information-box .box-icon {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 0 auto;
        margin-bottom: 60px;
        position: absolute;
        top: -60px;
        right: 0;
        left: 0;
        z-index: 0;
        background: #ffffff;
        -webkit-box-shadow: -5px 18px 28px 0px rgba(205, 205, 205, 0.35);
        -moz-box-shadow: -5px 18px 28px 0px rgba(205, 205, 205, 0.35);
        box-shadow: -5px 18px 28px 0px rgba(205, 205, 205, 0.35);
    }

    .information-box .box-icon img {
        position: absolute;
        left: 0;
        right: 0;
        top: 50%;
        z-index: 0;
        display: block;
        margin: 0 auto;
        -webkit-transform: translateY(-50%);
        -ms-transform: translateY(-50%);
        -o-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .information-box p {
        font-size: 16px;
        color: #a3a1a1;
    }

    .information-box p span {
        font-size: 18px;
        font-weight: 600;
        color: #503c57;
    }

    .ph-number {
        margin-top: 30px;
        font-size: 18px;
        font-weight: 600;
        color: #272626 !important;
    }

    .ph-number i {
        color: #3FEEF7;
        margin-right: 10px;
    }

    .contact-form-row {
        margin-top: 90px;
        background: url(@/assets/images/ContactComp/ContactUsStartComp/map.png);
        background-position: 50% 50%;
        background-repeat: no-repeat;
    }

    .contact-form-row .form-control {
        border: none;
        border-bottom: 1px solid #D8D8D8;
        margin-bottom: 40px;
        background: transparent;
    }

    .contact-form-row .errors {
        color: red;
        margin-bottom: 20px;
    }

    .contact-form-row textarea {
        min-height: 180px;
        resize: none;
    }
</style>