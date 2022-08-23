<script>
    export default {
        data: () => ({
            VFullName: '',
            VEmail: '',
            VPhone: '',
            VComment: '',
            VSuccessMessage: '',
            VSendToServer: false,
            VErrors: {}
        }),
        methods: {
            // Send Data To Server
            SubmitFormToServer() {
                this.$axios.post('/contact/',{
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
                <div class="col-lg-4 col-sm-12">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/static/images/ContactComp/ContactUsStartComp/contact-icon-1.png" alt="Icons">
                        </div>
                        <p><span>Address</span></p>
                        <p>Dash Bacary More, Gaibandha</p>
                    </div>
                </div>
                <div class="col-lg-4 col-sm-12">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/static/images/ContactComp/ContactUsStartComp/contact-icon-2.png" alt="Icons">
                        </div>
                        <p><span>Email Address</span></p>
                        <p>photosretouch.service@gmail.com</p>
                        <p>admin@photosretouch.com</p>
                    </div>
                </div>
                <div class="col-lg-4 col-sm-12">
                    <div class="information-box">
                        <div class="box-icon">
                            <img src="@/static/images/ContactComp/ContactUsStartComp/contact-icon-3.png" alt="Icons">
                        </div>
                        <p><span>Offie phone number</span></p>
                        <p class="ph-number mt-0"><i class="fa fa-microphone"></i> +880 1825 324 344</p>
                        <p class="ph-number mt-0"><i class="fa fa-microphone"></i> +880 1748 915 830</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
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
</style>