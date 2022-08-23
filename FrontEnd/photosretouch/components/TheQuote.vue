<script>
  export default {
    data: () => ({
      VSuccessMessage: '',
      fileuploader: true,
      VErrors: {},
      VName: '',
      VEmail: '',
      VService: [],
      VMessage: '',
      VFilelink: '',
      VImages: false,
      AllDataForServer: new FormData()
    }),
    methods: {
      GetSubmit() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        this.VErrors = {};
        if (!this.VName) {
            this.VErrors['name'] = 'Name Required.';
        }
        if (!this.VEmail) {
            this.VErrors['email'] = 'Email Required.';
        } else if (!this.validEmail(this.VEmail)) {
            this.VErrors['email'] = 'Please use a valid Email.';
        }
        if (this.VService.length === 0) {
            this.VErrors['service'] = 'Services Required.';
        }
        if (!this.VFilelink) {
            this.VErrors['filelink'] = 'Link Required.';
        }
        if (!this.Vimages) {
            this.VErrors['images'] = 'Images Required.';
        }
        if (!this.VErrors['name'] && !this.VErrors['email'] && !this.VErrors['service']) {
            if (this.fileuploader && !this.VErrors['images']){
              this.AllDataForServer.append("name", this.VName)
              this.AllDataForServer.append("email", this.VEmail)
              this.AllDataForServer.append("services_list", this.VService)
              this.AllDataForServer.append("message", this.VMessage)
              this.UncheckAll();
              this.SendToServer(this.AllDataForServer);
            }
            if (!this.fileuploader && !this.VErrors['filelink']){
              this.AllDataForServer.append("name", this.VName)
              this.AllDataForServer.append("email", this.VEmail)
              this.AllDataForServer.append("services_list", this.VService)
              this.AllDataForServer.append("message", this.VMessage)
              this.AllDataForServer.append("filelink", this.VFilelink)
              this.UncheckAll();
              this.SendToServer(this.AllDataForServer);
            }
        }
      },
      UncheckAll(){
        const CheckBox = document.querySelectorAll('.checkBox-input.checked-value')
        for (let i=0; i < CheckBox.length; i++){
          if (CheckBox[i].checked){
            CheckBox[i].click();
          }
        }
        document.querySelector('#images-list').innerHTML = '';
      },
      SendToServer(data){
        this.$axios.post('/quote/',data)
        .then(response => {
            this.VSuccessMessage = response.data['message'];
            this.VName = '';
            this.VEmail = '';
            this.VService = [];
            this.VMessage = '';
            this.VFilelink = '';
            this.AllDataForServer = [];
        }).catch(err => console.log(err.message))
      },
      validEmail(email) {
          let re =
              /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return re.test(email);
      },
      CheckCheckbox(e) {
        if (e.target.checked) {this.VService.push(e.target.value)}
        else {
          let ValueIndex = this.VService.indexOf(e.target.value);
          if (ValueIndex !== -1) {
            this.VService.splice(ValueIndex, 1);
          }
        }
      },
      checkUploadOption(e){
        if (e.target.value === 'WebFile'){
          this.fileuploader = true;
        } else if (e.target.value === 'LinkFile'){
          this.fileuploader = false;
        }
      },
    },
    computed: {
      AllServices() {
        return this.$store.state.services_info
      }
    },
    mounted() {
      const ImageUploader = document.querySelector('#ImageUploader');
      const fileUploadInput = document.querySelector('#file-upload');
      const ImagesList = document.querySelector('#images-list');
      fileUploadInput.addEventListener('change', () => {
        this.Vimages = true;
        let AllImages = fileUploadInput.files;
        for (let i = 0; i < AllImages.length; i++) {
            this.AllDataForServer.append("images", AllImages[i]);
            ImagesList.innerHTML += `
              <div class="single-img-box ml-2 mr-2">
                <div class="single-img">
                  <img src="${URL.createObjectURL(AllImages[i])}" alt="${AllImages[i].name}">
                </div>
                <p class="mb-0 text-center">${AllImages[i].name}</p>
              </div>`;
        }
      });
      ImageUploader.addEventListener('drop', event => {
        event.preventDefault();
        ImageUploader.classList.remove('dragover-active');
        let AllImages = event.dataTransfer.files;
        this.Vimages = true;
        for (let i = 0; i < AllImages.length; i++) {
            this.AllDataForServer.append("images", AllImages[i]);
            ImagesList.innerHTML += `
              <div class="single-img-box ml-2 mr-2">
                <div class="single-img">
                  <img src="${URL.createObjectURL(AllImages[i])}" alt="${AllImages[i].name}">
                </div>
                <p class="mb-0 text-center">${AllImages[i].name}</p>
              </div>`;
        }
      });
      ImageUploader.addEventListener('dragover', event => {
        event.preventDefault();
        ImageUploader.classList.add('dragover-active');
      });
      ImageUploader.addEventListener('dragleave', event => {
        event.preventDefault();
        ImageUploader.classList.remove('dragover-active');
      });
    }
  }

</script>

<template>
  <div>
    <!-- Page Name Start -->
    <section class="pt-8 pb-5 get-quote-page-name-area">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="d-flex flex-column text-center w-full mb-20">
              <h1 class="title mb-2 text-gray-900 uppercase">Get Your Quote
              </h1>
              <div class="mt-6">
                <div class="rounded rounded-pill text-separator d-inline-flex"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- getQuote section start -->
    <section class="container getQuote-section">
      <form @submit.prevent="GetSubmit">
        <h4 v-if="VSuccessMessage" class="text-center mb-5 success-message p-2">{{VSuccessMessage}}</h4>
        <div class="getQuote-section-inner">
          <div class="row">
            <div class="col-md-6">
              <label for="inputName">Name</label>
              <input type="text" class="form-control mb-0" v-model="VName" placeholder="Name">
              <p v-if="VErrors.name" class="pb-0 error-message">{{VErrors.name}}</p>
            </div>
            <div class="col-md-6">
              <label for="inputEmail">E-mail Address</label>
              <input type="text" class="form-control mb-0" v-model="VEmail" placeholder="name@gmail.com">
              <p v-if="VErrors.email" class="pb-0 error-message">{{VErrors.email}}</p>
            </div>
          </div>
          <div class="row choose-service-container mt-4">
            <div class="col-12">
              <label class="input-title-main">Choose Service</label>
            </div>
            <div class="col-md-4 mb-3 d-flex align-items-center form-check" 
              v-for="service in AllServices"
              :key="service.id">
              <input @click="CheckCheckbox" class="checkBox-input checked-value" type="checkbox" :value="service.name"
                :id="service.id">
              <label class="mb-0 checkBox-label" :for="service.id">
                {{service.name}}
              </label>
            </div>
            <div class="col-md-4 mb-3 d-flex align-items-center form-check ">
              <input @click="CheckCheckbox" class="checkBox-input" type="checkbox" value="other" id="othervalue">
              <label class="mb-0 checkBox-label" for="othervalue">
                Other
              </label>
            </div>
          </div>
          <p v-if="VErrors.service" class="pb-0 error-message">{{VErrors.service}}</p>
          <!-- textarea -->
          <div class="mt-4 form-group">
            <h4 class="input-title-textarea">Message (optional):</h4>
            <textarea class="form-control" v-model="VMessage" rows="5"></textarea>
          </div>
          <!-- upload options area  -->
          <div class="row choose-service-container mt-4">
            <div class="col-12">
              <label class="input-title-main">Upload Options</label>
            </div>
          </div>
          <div class="upload-options-container mt-4">
            <div class="form-check">
              <input @click="checkUploadOption" class="form-check-input" type="radio" name="flexRadioDefault" id="WebFileUploader" checked value="WebFile">
              <label class="form-check-label" for="WebFileUploader">
                Web File Uploader
              </label>
            </div>
            <div class="form-check">
              <input @click="checkUploadOption" class="form-check-input" type="radio" name="flexRadioDefault" id="LinkFileUploader" value="LinkFile">
              <label class="form-check-label" for="LinkFileUploader">
                Files Link
              </label>
            </div>
            <template v-if="fileuploader">
              <div class="file-upload-container my-4">
                <div class="file-upload-inner-div" id="ImageUploader">
                  <input class="file-upload-input" type="file" id="file-upload" multiple
                    accept="image/png, image/jpeg">
                  <h3 class="file-upload-text">Drop files here or 
                    <label for="file-upload" class="file-upload-btn">browse files</label>
                  </h3>
                </div>
                <p v-if="VErrors.images" class="pb-0 mt-3 text-center error-message">{{VErrors.images}}</p>
              </div>
              <div class="d-flex flex-wrap justify-content-center" id="images-list"></div>
            </template>

            <div v-else class="files-link-container my-4">
              <p class="mb-2">Please use the link where you uploaded the images and don't forget to check that the link is works well.</p>
              <input v-model="VFilelink" type="text" class=" form-control mb-0" placeholder="Provide link here">
              <p v-if="VErrors.filelink" class="pb-0 error-message">{{VErrors.filelink}}</p>
            </div>
            <div class="send-quote-btn-div d-flex justify-content-center py-5">
              <button type="submit" class="send-quote-btn border-0 rounded-pill text-white">Send Quote</button>
            </div>
          </div>
        </div>
      </form>
    </section>
    <!-- getQuote section end -->
  </div>
</template>

<style>
  .success-message {
    color: #fff;
    background-color: #2691BF;
  }
  .error-message {
    color: red;
    font-weight: bolder;
  }
  .choose-service-container label.checkBox-label,
  .form-check-label:hover {
    cursor: pointer;
  }
  /* get a quote page */
  .get-quote-page-name-area {
    padding: 150px 0 120px;
  }

  .getQuote-section-inner {
    padding: 0 120px;
  }

  .get-quote-page-name-area .title {
    font-size: 30px;
  }

  .getQuote-section input,
  .getQuote-section textarea {
    border-radius: 4px;
  }

  .getQuote-section .input-title-main {
    font-size: 24px;
    font-weight: 600;
  }

  .getQuote-section .input-title-textarea,
  .getQuote-section .input-title-upload {
    font-size: 20px;
    font-weight: 600;
    color: #4a5568;
  }

  .choose-service-container input[type=checkbox] {
    width: 17.6px;
    height: 17.6px;
    margin-right: 6px;
    accent-color: #2691BF;
  }

  .choose-service-container label {
    font-size: 14px;
    font-weight: 700;
  }

  .upload-options-container input[type=radio] {
    width: 17px;
    height: 17px;
    margin-right: 6px;
    accent-color: #2691BF;
  }

  .file-upload-container {
    background-color: #fafafa;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    height: 450px;
  }

  .file-upload-inner-div {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: calc(100% - 14px);
    margin: 7px;
    border-radius: 3px;
    border: 1px dashed #dfdfdf;
  }

  .file-upload-input {
    visibility: hidden;
  }

  .file-upload-text {
    font-size: 25px;
    font-weight: 400;
  }

  .file-upload-btn {
    color: #2691BF;
    border: 0;
    background-color: transparent;
    text-transform: initial;
    padding: 0px;
    line-height: 26px;
    border-bottom: 1px solid transparent;
    cursor: pointer;
  }

  .file-upload-btn:hover {
    border-bottom: 1px solid #3DEEF7;
  }

  .file-upload-btn:focus {
    outline: none;
  }


  .send-quote-btn {
    background-color: #3DEEF7;
    padding: 10px 35px;
    transition: .5s;
    font-size: 20px;
  }

  .send-quote-btn:focus {
    outline: none;
  }

  .send-quote-btn:hover {
    background-color: #2691BF;
  }

  .single-img-box {
    width: 200px;
  }

  .single-img {
    height: 200px;
    width: 200px;
  }

  .single-img img {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }

  .dragover-active {
    border: 7px solid #2691BF;
    margin: 0;
    height: 100%;
  }
  
  @media only screen and (max-width:991px) {
    /* get a quote page */
    .getQuote-section-inner {
      padding: 0;
    }
  }

</style>
